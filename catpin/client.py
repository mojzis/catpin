"""A small Pinboard v1 API client.

The auth token is read from the environment and only ever travels in the
query string of an outgoing request; it is never echoed, logged, or folded
into an exception message.
"""

from __future__ import annotations

import os
import time
from typing import Any

import httpx

from .errors import (
    ApiResultError,
    ApiStatusError,
    MalformedTokenError,
    MissingTokenError,
)

API_BASE = "https://api.pinboard.in/v1"
TOKEN_ENV = "PINBOARD_TOKEN"

#: Pinboard asks for at most one request per second for ordinary endpoints.
GENTLE_INTERVAL_S = 1.0
#: ...and at most one posts/all every five minutes.
ALL_INTERVAL_S = 300.0

_RATE_LIMITED = 429
_UNAUTHORIZED = 401


def read_token() -> str:
    """Return the configured token, without ever revealing it on failure."""
    raw = os.environ.get(TOKEN_ENV, "").strip()
    if not raw:
        raise MissingTokenError
    user, _, secret = raw.partition(":")
    if not user or not secret:
        raise MalformedTokenError
    return raw


def token_username() -> str:
    """Return just the username half of the token, safe to display."""
    return read_token().partition(":")[0]


class PinboardClient:
    """Rate-limited wrapper over the handful of endpoints this tool needs."""

    def __init__(
        self,
        token: str | None = None,
        timeout: float = 60.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self._token = token or read_token()
        self._http = httpx.Client(
            timeout=timeout,
            headers={"User-Agent": "catpin/0.1 (+personal pin tagger)"},
            follow_redirects=True,
            transport=transport,
        )
        self._last_call = 0.0

    def __enter__(self) -> PinboardClient:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def close(self) -> None:
        """Release the underlying HTTP connection pool."""
        self._http.close()

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_call
        if self._last_call and elapsed < GENTLE_INTERVAL_S:
            time.sleep(GENTLE_INTERVAL_S - elapsed)

    def _get(self, endpoint: str, **params: str) -> Any:
        self._throttle()
        query = {**params, "auth_token": self._token, "format": "json"}
        response = self._http.get(f"{API_BASE}/{endpoint}", params=query)
        self._last_call = time.monotonic()
        if response.status_code in (_UNAUTHORIZED, _RATE_LIMITED):
            raise ApiStatusError(endpoint, response.status_code)
        if response.status_code >= httpx.codes.BAD_REQUEST:
            raise ApiStatusError(endpoint, response.status_code)
        return response.json()

    # -- read endpoints ---------------------------------------------------

    def posts_all(self, fromdt: str | None = None) -> list[dict[str, Any]]:
        """Every pin, or every pin created at/after an ISO-8601 UTC instant."""
        params = {"fromdt": fromdt} if fromdt else {}
        payload = self._get("posts/all", **params)
        return list(payload)

    def posts_recent(self, count: int = 100) -> list[dict[str, Any]]:
        """The most recent pins; cheap enough to call often."""
        payload = self._get("posts/recent", count=str(count))
        return list(payload.get("posts", []))

    def tags_get(self) -> dict[str, int]:
        """Tag -> use count, as Pinboard reports it."""
        payload = self._get("tags/get")
        return {tag: int(count) for tag, count in payload.items()}

    def posts_update(self) -> str:
        """ISO-8601 timestamp of the most recent change to the account."""
        return str(self._get("posts/update")["update_time"])

    # -- write endpoints --------------------------------------------------

    def tags_rename(self, old: str, new: str) -> None:
        """Rename a tag, merging into ``new`` when that tag already exists."""
        payload = self._get("tags/rename", old=old, new=new)
        result = str(payload.get("result", ""))
        if result != "done":
            raise ApiResultError("tags/rename", result or "unknown error")

    def posts_add(self, fields: dict[str, str]) -> None:
        """Create or replace a pin. Callers must pass every field to keep."""
        payload = self._get("posts/add", **fields)
        result = str(payload.get("result_code", ""))
        if result != "done":
            raise ApiResultError("posts/add", result or "unknown error")
