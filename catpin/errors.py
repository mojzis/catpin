"""Errors raised by the Pinboard client.

Messages are built inside the classes so that no caller can accidentally
interpolate the auth token into an error string.
"""

from __future__ import annotations


class PinboardError(RuntimeError):
    """Base class for Pinboard configuration and API failures."""


class MissingTokenError(PinboardError):
    """PINBOARD_TOKEN is absent from the environment."""

    def __init__(self) -> None:
        super().__init__("PINBOARD_TOKEN is not set (expected 'username:HEX')")


class MalformedTokenError(PinboardError):
    """PINBOARD_TOKEN is present but not in 'username:HEX' form."""

    def __init__(self) -> None:
        super().__init__("PINBOARD_TOKEN is malformed (expected 'username:HEX')")


class ApiStatusError(PinboardError):
    """The API answered with a non-success status.

    Only the endpoint path and the status code are reported; the request URL
    carries the auth token and is deliberately never included.
    """

    def __init__(self, endpoint: str, status: int) -> None:
        super().__init__(f"{endpoint}: HTTP {status}")
        self.endpoint = endpoint
        self.status = status


class ApiResultError(PinboardError):
    """The API answered 200 but the payload reported a failure."""

    def __init__(self, endpoint: str, result: str) -> None:
        super().__init__(f"{endpoint}: {result}")
        self.endpoint = endpoint
        self.result = result


class MissingCacheError(PinboardError):
    """A cached file the command needs has not been fetched yet."""

    def __init__(self, path: str) -> None:
        super().__init__(f"{path} not found - run 'fetch' first")
