"""The analyse command, driven end to end over a temporary data/ directory."""

import json

import pytest
from typer.testing import CliRunner

from catpin.cli import app

runner = CliRunner()


@pytest.fixture
def workspace(tmp_path, monkeypatch, pins):
    """A temporary working directory holding a cached archive."""
    monkeypatch.chdir(tmp_path)
    data = tmp_path / "data"
    data.mkdir()
    (data / "pins_raw.json").write_text(json.dumps(pins))
    return tmp_path


def test_analyse_writes_the_report_and_the_digest(workspace):
    result = runner.invoke(app, ["analyse"])
    assert result.exit_code == 0
    assert (workspace / "data" / "analysis.md").exists()
    assert (workspace / "data" / "stats.json").exists()


def test_analyse_reports_the_totals_it_found(workspace):
    result = runner.invoke(app, ["analyse"])
    assert "9 pins, 10 tags" in result.stdout


def test_analyse_keeps_hand_written_notes_on_a_second_run(workspace):
    runner.invoke(app, ["analyse"])
    report = workspace / "data" / "analysis.md"
    report.write_text(report.read_text() + "\n## Decisions\n\nkeep `python`.\n")
    runner.invoke(app, ["analyse"])
    assert "## Decisions" in report.read_text()


def test_analyse_without_a_cached_archive_explains_the_fix(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["analyse"])
    assert result.exit_code != 0
    assert "fetch" in str(result.exception)
