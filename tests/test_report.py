"""The rendered report must carry every section and survive a re-run."""

from datetime import UTC, datetime

import pytest

from catpin.analysis import Stats, toread_backlog
from catpin.report import CURATED_MARKER, merge_curated, render, stats_payload

NOW = datetime(2023, 3, 1, tzinfo=UTC)


@pytest.fixture
def document(pins):
    """The analysis rendered from the synthetic archive."""
    return render(Stats(pins=pins, now=NOW), toread_backlog(pins, NOW), "2023-03-01")


@pytest.mark.parametrize(
    "heading",
    [
        "## Overview",
        "## Cadence",
        "## Tagging hygiene",
        "## Tag frequency",
        "## Near-duplicate tags",
        "## Tag co-occurrence",
        "## Top domains",
        "## `toread` backlog",
        "## How the tagging style changed",
        "## Mechanical merge candidates",
    ],
)
def test_report_contains_every_section(document, heading):
    assert heading in document


def test_report_marks_empty_months_with_a_dot(document):
    assert "| 2021 | 2 | . |" in document


def test_report_proposes_folding_the_rare_spelling_into_the_common_one(document):
    assert "| `Python` | 1 | `python` | 2 |" in document


def test_merge_curated_keeps_hand_written_text_across_a_rerun(document):
    edited = document + "\n## My vocabulary\n\nkeep `python`.\n"
    assert "## My vocabulary" in merge_curated(document, edited)


def test_merge_curated_accepts_a_first_run_with_no_previous_file(document):
    assert merge_curated(document, None) == document


def test_curated_marker_is_the_last_thing_rendered(document):
    assert document.rstrip().endswith(CURATED_MARKER)


def test_stats_payload_is_json_shaped(pins):
    stats = Stats(pins=pins, now=NOW)
    payload = stats_payload(stats, toread_backlog(pins, NOW))
    assert payload["total_pins"] == 9
    assert payload["tag_counts"]["python"] == 2
    assert payload["variant_groups"][0]["kinds"] == ["case"]
