"""Filesystem layout for cached Pinboard data and generated reports."""

from __future__ import annotations

from pathlib import Path

DATA_DIR = Path("data")

PINS_RAW = DATA_DIR / "pins_raw.json"
PINS_CLEAN = DATA_DIR / "pins_clean.json"
TAGS_RAW = DATA_DIR / "tags_raw.json"
ANALYSIS_MD = DATA_DIR / "analysis.md"
STATS_JSON = DATA_DIR / "stats.json"
STATE_JSON = DATA_DIR / "state.json"
INBOX_JSON = DATA_DIR / "inbox.json"
PROPOSALS_JSON = DATA_DIR / "proposals.json"
VOCABULARY_MD = DATA_DIR / "vocabulary.md"
