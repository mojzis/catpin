"""Command line entry point."""

from __future__ import annotations

import time
from datetime import UTC, datetime

import typer

from . import config
from .analysis import Stats, toread_backlog
from .client import ALL_INTERVAL_S, PinboardClient, token_username
from .report import merge_curated, render, stats_payload
from .state import load_state, read_json, save_state, write_json

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Analyse a Pinboard archive and tag fresh pins.",
)


def _archive_is_fresh(force: bool) -> float:
    """Seconds still to wait before ``posts/all`` may be called again."""
    if force:
        return 0.0
    last = float(load_state(config.STATE_JSON).get("archive_fetched_epoch", 0.0))
    return max(0.0, ALL_INTERVAL_S - (time.time() - last))


@app.command()
def archive(
    force: bool = typer.Option(
        False, "--force", help="Ignore the five-minute posts/all cooldown."
    ),
) -> None:
    """Fetch the whole archive and the tag list into data/ (Phase 1)."""
    if config.PINS_RAW.exists() and not force:
        wait = _archive_is_fresh(force)
        if wait:
            typer.echo(
                f"cached {config.PINS_RAW} is younger than the posts/all limit; "
                f"{wait / 60:.1f} min left (--force to override)"
            )
            raise typer.Exit(0)

    with PinboardClient() as client:
        typer.echo(f"account {token_username()}")
        pins = client.posts_all()
        write_json(config.PINS_RAW, pins)
        typer.echo(f"{config.PINS_RAW} {len(pins)} pins")

        tags = client.tags_get()
        write_json(config.TAGS_RAW, tags)
        typer.echo(f"{config.TAGS_RAW} {len(tags)} tags")

    save_state(
        config.STATE_JSON,
        archive_fetched_epoch=time.time(),
        archive_fetched_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )


@app.command()
def analyse() -> None:
    """Rebuild data/analysis.md and data/stats.json from the cache."""
    pins = read_json(config.PINS_RAW)
    now = datetime.now(UTC)
    stats = Stats(pins=pins, now=now)
    backlog = toread_backlog(pins, now)

    existing = config.ANALYSIS_MD.read_text() if config.ANALYSIS_MD.exists() else None
    document = render(stats, backlog, now.strftime("%Y-%m-%d"))
    config.ANALYSIS_MD.parent.mkdir(parents=True, exist_ok=True)
    config.ANALYSIS_MD.write_text(merge_curated(document, existing))
    write_json(config.STATS_JSON, stats_payload(stats, backlog))

    typer.echo(f"{config.ANALYSIS_MD} {stats.total} pins, {len(stats.counts)} tags")
    typer.echo(f"{config.STATS_JSON} written")


if __name__ == "__main__":
    app()
