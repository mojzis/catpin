"""Shared fixtures: a small synthetic archive shaped like Pinboard's JSON."""

from __future__ import annotations

from typing import Any

import pytest


def make_pin(
    time: str,
    tags: str = "",
    href: str = "https://example.com/a",
    toread: str = "no",
) -> dict[str, Any]:
    """One pin in the shape ``posts/all`` returns."""
    return {
        "href": href,
        "description": "A title",
        "extended": "",
        "meta": "abc",
        "hash": "def",
        "time": time,
        "shared": "yes",
        "toread": toread,
        "tags": tags,
    }


@pytest.fixture
def pins() -> list[dict[str, Any]]:
    """Nine pins spread over three years with deliberate tag messiness."""
    return [
        make_pin("2021-01-05T10:00:00Z", "python tool", "https://www.github.com/x"),
        make_pin("2021-01-20T10:00:00Z", "Python paper", "https://arxiv.org/abs/1"),
        make_pin("2021-03-02T10:00:00Z", "", "https://github.com/y"),
        make_pin("2022-06-11T10:00:00Z", "python papers", "https://arxiv.org/abs/2"),
        make_pin("2022-06-12T10:00:00Z", "toread", "https://example.com/b", "yes"),
        make_pin("2022-07-01T10:00:00Z", "energy", "https://example.com/c"),
        make_pin("2023-02-01T10:00:00Z", "python-dev tool", "https://github.com/z"),
        make_pin("2023-02-02T10:00:00Z", "python_dev", "https://example.com/d", "yes"),
        make_pin(
            "2023-02-03T10:00:00Z", "energy grid toread", "https://example.com/e", "yes"
        ),
    ]
