"""The small JSON helpers behind data/."""

import pytest

from catpin.errors import MissingCacheError
from catpin.state import load_state, read_json, save_state, write_json


def test_write_json_creates_missing_parent_directories(tmp_path):
    target = tmp_path / "data" / "nested" / "pins.json"
    write_json(target, [1, 2, 3])
    assert read_json(target) == [1, 2, 3]


def test_write_json_keeps_non_ascii_readable(tmp_path):
    target = tmp_path / "tags.json"
    write_json(target, {"energie": 3})
    assert "energie" in target.read_text()


def test_read_json_names_the_fix_when_the_cache_is_absent(tmp_path):
    with pytest.raises(MissingCacheError) as raised:
        read_json(tmp_path / "pins_raw.json")
    assert "fetch" in str(raised.value)


def test_load_state_of_a_first_run_is_empty(tmp_path):
    assert load_state(tmp_path / "state.json") == {}


def test_save_state_merges_rather_than_replaces(tmp_path):
    path = tmp_path / "state.json"
    save_state(path, last_run="2026-01-01")
    merged = save_state(path, cursor="2026-02-01")
    assert merged == {"last_run": "2026-01-01", "cursor": "2026-02-01"}
