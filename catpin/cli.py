"""Command line entry point."""

from __future__ import annotations

import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer

from . import config
from .analysis import Stats, pin_tags, tag_span, toread_backlog
from .areas import classify, load_seeds
from .clean import clean_pins
from .client import ALL_INTERVAL_S, PinboardClient, token_username
from .renames import Rename, default_groups, plan_renames, select
from .report import merge_curated, render, stats_payload
from .state import load_state, read_json, save_state, write_json

RENAMES_JSON = Path("renames.json")
AREAS_JSON = Path("areas.json")

#: A tag whose pins all land inside this many days looks like a burst.
BURST_DAYS = 60

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
    force: Annotated[
        bool,
        typer.Option("--force", help="Ignore the five-minute posts/all cooldown."),
    ] = False,
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
    source = config.PINS_CLEAN if config.PINS_CLEAN.exists() else config.PINS_RAW
    pins = read_json(source)
    now = datetime.now(UTC)
    stats = Stats(pins=pins, now=now)
    backlog = toread_backlog(pins, now)

    existing = config.ANALYSIS_MD.read_text() if config.ANALYSIS_MD.exists() else None
    document = render(stats, backlog, now.strftime("%Y-%m-%d"))
    config.ANALYSIS_MD.parent.mkdir(parents=True, exist_ok=True)
    config.ANALYSIS_MD.write_text(merge_curated(document, existing))
    write_json(config.STATS_JSON, stats_payload(stats, backlog))

    typer.echo(f"source {source}")
    typer.echo(f"{config.ANALYSIS_MD} {stats.total} pins, {len(stats.counts)} tags")
    typer.echo(f"{config.STATS_JSON} written")


if __name__ == "__main__":
    app()


def _rename_line(item: Rename, note: str = "") -> str:
    """One terse line describing a single rename."""
    arrow = f"{item.old} -> {item.new}"
    counts = (
        f"{item.old_uses}+{item.new_uses}={item.result_uses}"
        if item.merges
        else f"{item.old_uses}"
    )
    return f"  {arrow:38s} {counts:14s} {item.group:10s} {note}".rstrip()


@app.command()
def rename(
    group: Annotated[
        list[str] | None,
        typer.Option("--group", "-g", help="Only these groups from renames.json."),
    ] = None,
    yes: Annotated[
        bool, typer.Option("--yes", help="Actually rename. Default is a dry run.")
    ] = False,
) -> None:
    """Merge duplicate tags via tags/rename. Dry run unless --yes."""
    plan = read_json(RENAMES_JSON)
    counts = read_json(config.TAGS_RAW)
    items = plan_renames(plan, counts, list(group) if group else None)

    live = [i for i in items if i.exists]
    absent = [i for i in items if not i.exists]

    for item in live:
        typer.echo(_rename_line(item, "merge" if item.merges else ""))
    for item in absent:
        typer.echo(_rename_line(item, "SKIP: not in tags/get"))

    typer.echo(f"{len(live)} to apply, {len(absent)} skipped")
    if not yes:
        typer.echo("dry run; pass --yes to apply")
        raise typer.Exit(0)

    with PinboardClient() as client:
        for item in live:
            client.tags_rename(item.old, item.new)
            typer.echo(f"  done {item.old} -> {item.new}")
        after = client.tags_get()

    write_json(config.TAGS_RAW, after)
    stuck = [i.old for i in live if i.old in after]
    typer.echo(f"{len(live) - len(stuck)}/{len(live)} took effect")
    if stuck:
        typer.echo(f"still present after rename: {', '.join(stuck)}")
    save_state(
        config.STATE_JSON, renamed_at=datetime.now(UTC).isoformat(timespec="seconds")
    )


@app.command()
def clean(
    group: Annotated[
        list[str] | None,
        typer.Option("--group", "-g", help="Groups from renames.json to apply."),
    ] = None,
    revert: Annotated[
        bool, typer.Option("--revert", help="Delete the cleaned copy and stop.")
    ] = False,
) -> None:
    """Apply renames.json to a local copy of the archive. Pinboard is untouched."""
    if revert:
        config.PINS_CLEAN.unlink(missing_ok=True)
        typer.echo(f"removed {config.PINS_CLEAN}; analyse falls back to the raw cache")
        raise typer.Exit(0)

    plan = read_json(RENAMES_JSON)
    chosen = list(group) if group else default_groups(plan)
    mapping = select(plan, chosen)
    result = clean_pins(read_json(config.PINS_RAW), mapping)

    for fold, pins_touched in result.applied.most_common():
        typer.echo(f"  {fold:38s} {pins_touched} pins")

    dead = sorted(set(mapping) - {f.split(" -> ")[0] for f in result.applied})
    for fold in dead:
        typer.echo(f"  {fold:38s} 0 pins - not in this archive")

    write_json(config.PINS_CLEAN, result.pins)
    typer.echo(
        f"{config.PINS_CLEAN} {result.tags_before} -> {result.tags_after} tags, "
        f"{result.pins_changed} pin edits, {result.collapsed} duplicates collapsed"
    )
    typer.echo(f"groups: {', '.join(chosen or [])}; raw cache untouched")


@app.command()
def show(
    tag: Annotated[str, typer.Argument(help="The tag to inspect.")],
    limit: Annotated[
        int, typer.Option("--limit", "-n", help="How many pins to print.")
    ] = 20,
) -> None:
    """Print the pins carrying a tag, to check meaning before folding it."""
    source = config.PINS_CLEAN if config.PINS_CLEAN.exists() else config.PINS_RAW
    pins = read_json(source)
    hits = [p for p in pins if tag in pin_tags(p)]
    if not hits:
        typer.echo(f"{tag}: no pins")
        raise typer.Exit(1)

    days, first, last = tag_span(pins, tag)
    shape = "burst" if len(hits) > 1 and days <= BURST_DAYS else "spread"
    typer.echo(f"{tag}: {len(hits)} pins, {first}..{last}, {days}d span, {shape}")
    for pin in sorted(hits, key=lambda p: str(p.get("time", "")), reverse=True)[:limit]:
        typer.echo(f"  {str(pin.get('time', ''))[:10]}  [{pin.get('tags', '')}]")
        typer.echo(f"    {str(pin.get('description', ''))[:72]}")
        typer.echo(f"    {str(pin.get('href', ''))[:72]}")


def _source() -> Path:
    """The cleaned archive when one exists, otherwise the raw cache."""
    return config.PINS_CLEAN if config.PINS_CLEAN.exists() else config.PINS_RAW


@app.command()
def area(
    show_ambiguous: Annotated[
        bool, typer.Option("--ambiguous", help="List the undecidable pins.")
    ] = False,
) -> None:
    """Guess each pin's area of life from areas.json. Read-only."""
    seeds, neutral = load_seeds(read_json(AREAS_JSON))
    result = classify(read_json(_source()), seeds, neutral)

    for label, count in result.counts.most_common():
        typer.echo(f"  {label:16s} {count:5d}  {result.share(label):5.1f}%")
    typer.echo(f"{result.total} pins, {len(seeds)} areas, {len(neutral)} neutral tags")

    if show_ambiguous:
        for pin in result.ambiguous:
            typer.echo(
                f"  [{pin.get('tags', '')}] {str(pin.get('description', ''))[:60]}"
            )


@app.command()
def burst(
    days: Annotated[
        int, typer.Option("--days", help="Longest span still counted as a burst.")
    ] = BURST_DAYS,
    min_pins: Annotated[int, typer.Option("--min-pins", help="Ignore rarer tags.")] = 2,
) -> None:
    """List tags whose pins all land within a few days - hunts and binges."""
    pins = read_json(_source())
    seen: dict[str, list[str]] = {}
    for pin in pins:
        for tag in pin_tags(pin):
            seen.setdefault(tag, []).append(str(pin.get("time", "")))

    rows = []
    for tag, times in seen.items():
        if len(times) < min_pins:
            continue
        span, first, last = tag_span(pins, tag)
        if span <= days:
            rows.append((span, -len(times), tag, len(times), first, last))

    for span, _, tag, count, first, last in sorted(rows):
        typer.echo(f"  {tag:20s} {count:3d} pins  {span:4d}d  {first}..{last}")
    typer.echo(f"{len(rows)} burst tags of {len(seen)} ({days}d, {min_pins}+ pins)")
