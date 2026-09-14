#!/usr/bin/env python3
"""Thin wrapper so the tool runs as `uv run pins.py ...` from the repo root."""

from catpin.cli import app

if __name__ == "__main__":
    app()
