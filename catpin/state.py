"""Tiny JSON helpers for the files under ``data/``."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import MissingCacheError


def write_json(path: Path, payload: Any) -> None:
    """Write ``payload`` as indented JSON, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def read_json(path: Path) -> Any:
    """Read JSON, with a message that names the fix when the file is absent."""
    if not path.exists():
        raise MissingCacheError(str(path))
    return json.loads(path.read_text())


def load_state(path: Path) -> dict[str, Any]:
    """The run state, or an empty dict on a first run."""
    if not path.exists():
        return {}
    loaded = json.loads(path.read_text())
    return dict(loaded) if isinstance(loaded, dict) else {}


def save_state(path: Path, **updates: Any) -> dict[str, Any]:
    """Merge ``updates`` into the stored state and persist it."""
    state = load_state(path)
    state.update(updates)
    write_json(path, state)
    return state
