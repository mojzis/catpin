"""Client behaviour, above all that the auth token never escapes."""

import httpx
import pytest

from catpin.client import PinboardClient, read_token, token_username
from catpin.errors import (
    ApiResultError,
    ApiStatusError,
    MalformedTokenError,
    MissingTokenError,
)

TOKEN = "alice:0123456789ABCDEF"


def client_returning(status: int, payload: object) -> PinboardClient:
    """A client wired to a transport that always answers the same way."""
    transport = httpx.MockTransport(
        lambda request: httpx.Response(status, json=payload)
    )
    return PinboardClient(token=TOKEN, transport=transport)


def test_read_token_rejects_an_absent_variable(monkeypatch):
    monkeypatch.delenv("PINBOARD_TOKEN", raising=False)
    with pytest.raises(MissingTokenError):
        read_token()


def test_read_token_rejects_a_token_without_a_username(monkeypatch):
    monkeypatch.setenv("PINBOARD_TOKEN", "deadbeef")
    with pytest.raises(MalformedTokenError):
        read_token()


def test_token_username_exposes_only_the_username_half(monkeypatch):
    monkeypatch.setenv("PINBOARD_TOKEN", TOKEN)
    assert token_username() == "alice"


def test_missing_token_error_does_not_quote_any_token(monkeypatch):
    monkeypatch.setenv("PINBOARD_TOKEN", TOKEN)
    monkeypatch.delenv("PINBOARD_TOKEN")
    with pytest.raises(MissingTokenError) as raised:
        read_token()
    assert "0123456789ABCDEF" not in str(raised.value)


def test_api_error_reports_the_status_without_the_request_url():
    with client_returning(401, {}) as client, pytest.raises(ApiStatusError) as raised:
        client.posts_all()
    assert str(raised.value) == "posts/all: HTTP 401"
    assert "auth_token" not in str(raised.value)


def test_server_error_is_reported_as_a_pinboard_error():
    with client_returning(503, {}) as client, pytest.raises(ApiStatusError) as raised:
        client.tags_get()
    assert raised.value.status == 503


def test_posts_all_returns_the_pin_list():
    with client_returning(
        200, [{"href": "https://example.com", "tags": "x"}]
    ) as client:
        assert client.posts_all() == [{"href": "https://example.com", "tags": "x"}]


def test_tags_get_converts_counts_to_integers():
    with client_returning(200, {"python": "42"}) as client:
        assert client.tags_get() == {"python": 42}


def test_posts_recent_unwraps_the_posts_key():
    with client_returning(200, {"posts": [{"href": "https://example.com"}]}) as client:
        assert client.posts_recent() == [{"href": "https://example.com"}]


def test_posts_add_sends_every_field_it_is_given():
    seen: list[httpx.URL] = []

    def record(request: httpx.Request) -> httpx.Response:
        seen.append(request.url)
        return httpx.Response(200, json={"result_code": "done"})

    with PinboardClient(token=TOKEN, transport=httpx.MockTransport(record)) as client:
        client.posts_add({"url": "https://pinned.test/a", "replace": "yes"})
    assert seen[0].params["url"] == "https://pinned.test/a"
    assert seen[0].params["replace"] == "yes"


def test_posts_add_raises_on_any_other_result():
    with (
        client_returning(200, {"result_code": "must provide title"}) as client,
        pytest.raises(ApiResultError),
    ):
        client.posts_add({"url": "https://pinned.test/a"})


def test_the_token_travels_in_the_query_string():
    seen: list[httpx.URL] = []

    def record(request: httpx.Request) -> httpx.Response:
        seen.append(request.url)
        return httpx.Response(200, json=[])

    with PinboardClient(token=TOKEN, transport=httpx.MockTransport(record)) as client:
        client.posts_all()
    assert seen[0].params["auth_token"] == TOKEN
    assert seen[0].params["format"] == "json"
