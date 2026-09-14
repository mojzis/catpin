"""Render the archive analysis as Markdown."""

from __future__ import annotations

from collections import Counter
from typing import Any

from .analysis import Stats, cooccurrence, neighbours, quiet_runs, tags_per_year
from .tagnorm import typo_candidates, variant_groups

CURATED_MARKER = "<!-- CURATED: hand-written below this line; analyse preserves it -->"

MONTH_HEADS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

HEAD_TAGS = 40
TOP_DOMAINS = 25
CLUSTER_TAGS = 20
#: A tag below this many uses is long tail rather than working vocabulary.
ESTABLISHED_USES = 5

_ONCE = 1
_TWICE = 2


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    """A GitHub-flavoured Markdown table."""
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    lines.append("")
    return lines


def _pct(part: int, whole: int) -> str:
    """``part`` as a percentage of ``whole``, or ``-`` when undefined."""
    return f"{100 * part / whole:.1f}%" if whole else "-"


def _overview(stats: Stats) -> list[str]:
    months = stats.months
    active = [m for m, n in months.items() if n]
    first, last = (min(months), max(months)) if months else ("-", "-")
    busiest = sorted(months.items(), key=lambda kv: -kv[1])[:5]
    return [
        "## Overview",
        "",
        *_table(
            ["metric", "value"],
            [
                ["pins", str(stats.total)],
                ["first month", first],
                ["last month", last],
                ["months spanned", str(len(months))],
                ["months with at least one pin", str(len(active))],
                [
                    "mean pins / active month",
                    f"{stats.total / len(active):.1f}" if active else "-",
                ],
                ["distinct tags", str(len(stats.counts))],
                ["distinct domains", str(len(stats.domains))],
            ],
        ),
        "Busiest months: " + ", ".join(f"{m} ({n})" for m, n in busiest) + ".",
        "",
    ]


def _cadence(stats: Stats) -> list[str]:
    months = stats.months
    by_year: dict[int, list[int]] = {}
    for month, count in months.items():
        year, index = int(month[:4]), int(month[5:]) - 1
        by_year.setdefault(year, [0] * 12)[index] = count

    rows = [
        [str(year), *[str(n) if n else "." for n in values], f"**{sum(values)}**"]
        for year, values in sorted(by_year.items())
    ]
    lines = [
        "## Cadence",
        "",
        "Pins per month over the whole history (`.` is a month with no pins).",
        "",
        *_table(["year", *MONTH_HEADS, "total"], rows),
    ]

    gaps = quiet_runs(months)
    if gaps:
        lines += [
            "Quiet stretches of two months or more:",
            "",
            *_table(
                ["from", "to", "months"],
                [[start, end, str(length)] for start, end, length in gaps[:10]],
            ),
        ]
    else:
        lines += ["No gap of two consecutive empty months.", ""]
    return lines


def _hygiene(stats: Stats) -> list[str]:
    total = stats.total
    return [
        "## Tagging hygiene",
        "",
        *_table(
            ["group", "pins", "share"],
            [
                [
                    "untagged",
                    str(len(stats.untagged)),
                    _pct(len(stats.untagged), total),
                ],
                [
                    "exactly one tag",
                    str(len(stats.single_tag)),
                    _pct(len(stats.single_tag), total),
                ],
                [
                    "only workflow tags (no subject)",
                    str(len(stats.action_only)),
                    _pct(len(stats.action_only), total),
                ],
                [
                    "two or more tags",
                    str(total - len(stats.untagged) - len(stats.single_tag)),
                    _pct(total - len(stats.untagged) - len(stats.single_tag), total),
                ],
            ],
        ),
    ]


def _frequency(stats: Stats) -> list[str]:
    counts = stats.counts
    total_uses = sum(counts.values())
    ranked = counts.most_common()
    once = [t for t, n in ranked if n == _ONCE]
    twice = [t for t, n in ranked if n == _TWICE]
    head = ranked[:HEAD_TAGS]
    head_share = sum(n for _, n in head)

    lines = [
        "## Tag frequency",
        "",
        *_table(
            ["metric", "value"],
            [
                ["distinct tags", str(len(counts))],
                ["total tag uses", str(total_uses)],
                [
                    f"share of uses held by the top {HEAD_TAGS}",
                    _pct(head_share, total_uses),
                ],
                [
                    "tags used exactly once",
                    f"{len(once)} ({_pct(len(once), len(counts))})",
                ],
                [
                    "tags used exactly twice",
                    f"{len(twice)} ({_pct(len(twice), len(counts))})",
                ],
                [
                    f"tags used {ESTABLISHED_USES} or more times",
                    str(sum(1 for _, n in ranked if n >= ESTABLISHED_USES)),
                ],
            ],
        ),
        f"### Head: top {HEAD_TAGS} tags",
        "",
        *_table(
            ["#", "tag", "pins", "share of all pins"],
            [
                [str(i), tag, str(n), _pct(n, stats.total)]
                for i, (tag, n) in enumerate(head, start=1)
            ],
        ),
    ]
    if once:
        sample = ", ".join(f"`{t}`" for t in sorted(once)[:60])
        lines += [
            "### Long tail",
            "",
            f"{len(once)} tags are used once. First 60 alphabetically: {sample}.",
            "",
        ]
    return lines


def _duplicates(stats: Stats) -> list[str]:
    counts = dict(stats.counts)
    groups = variant_groups(counts)
    typos = typo_candidates(counts)

    lines = ["## Near-duplicate tags", ""]
    if groups:
        lines += [
            "Tags that collapse to the same key once case, separators and "
            "plurals are folded.",
            "",
            *_table(
                ["kind", "variants (uses)", "combined"],
                [
                    [
                        "+".join(group.kinds),
                        ", ".join(f"`{t}` ({n})" for t, n in group.members),
                        str(group.total),
                    ]
                    for group in groups
                ],
            ),
        ]
    else:
        lines += ["No case / separator / plural collisions found.", ""]

    if typos:
        lines += [
            "### Suspected typos",
            "",
            "A rare tag one character away from a much more common one.",
            "",
            *_table(
                ["suspect", "uses", "likely meant", "uses"],
                [[f"`{r}`", str(rn), f"`{c}`", str(cn)] for r, c, rn, cn in typos],
            ),
        ]
    return lines


def _clusters(stats: Stats) -> list[str]:
    counts = stats.counts
    pairs = cooccurrence(stats.pins)
    lines = [
        "## Tag co-occurrence",
        "",
        "For each frequent tag, the tags it shares pins with most often "
        "(Jaccard similarity).",
        "",
    ]
    rows = []
    for tag, _ in counts.most_common(CLUSTER_TAGS):
        partners = neighbours(pairs, counts, tag)
        if not partners:
            continue
        rows.append(
            [
                f"`{tag}`",
                ", ".join(
                    f"`{other}` {shared}/{sim}" for other, shared, sim in partners
                ),
            ]
        )
    lines += _table(["tag", "travels with (shared pins / jaccard)"], rows)

    strongest = sorted(
        (
            (left, right, shared, shared / (counts[left] + counts[right] - shared))
            for (left, right), shared in pairs.items()
        ),
        key=lambda row: -row[3],
    )[:15]
    lines += [
        "### Tightest pairs",
        "",
        *_table(
            ["pair", "shared pins", "jaccard"],
            [
                [f"`{a}` + `{b}`", str(shared), f"{sim:.2f}"]
                for a, b, shared, sim in strongest
            ],
        ),
    ]
    return lines


def _domains(stats: Stats) -> list[str]:
    ranked = stats.domains.most_common(TOP_DOMAINS)
    return [
        "## Top domains",
        "",
        *_table(
            ["#", "domain", "pins", "share"],
            [
                [str(i), host, str(n), _pct(n, stats.total)]
                for i, (host, n) in enumerate(ranked, start=1)
            ],
        ),
    ]


def _backlog(backlog: dict[str, Any]) -> list[str]:
    buckets = backlog["age_buckets"]
    return [
        "## `toread` backlog",
        "",
        *_table(
            ["metric", "value"],
            [
                ["pins marked toread", str(backlog["count"])],
                ["share of archive", f"{backlog['share_pct']}%"],
                ["median age", f"{backlog['median_age_days']} days"],
                ["oldest", f"{backlog['oldest_age_days']} days"],
                ["of those, untagged", str(backlog["untagged"])],
            ],
        ),
        *_table(
            ["age", "pins"],
            [[label, str(buckets.get(label, 0))] for label in buckets],
        ),
    ]


def _style(stats: Stats) -> list[str]:
    yearly = tags_per_year(stats.pins)
    return [
        "## How the tagging style changed",
        "",
        *_table(
            ["year", "pins", "mean tags / pin", "untagged", "single tag"],
            [
                [
                    str(year),
                    str(int(row["pins"])),
                    f"{row['mean_tags']:.2f}",
                    f"{row['untagged_pct']}%",
                    f"{row['single_tag_pct']}%",
                ]
                for year, row in yearly.items()
            ],
        ),
    ]


def _merges(stats: Stats) -> list[str]:
    counts = dict(stats.counts)
    rows = []
    for group in variant_groups(counts):
        target = group.winner
        for member, uses in group.members[1:]:
            rows.append([f"`{member}`", str(uses), f"`{target}`", str(counts[target])])
    for rare, common, rare_n, common_n in typo_candidates(counts):
        rows.append([f"`{rare}`", str(rare_n), f"`{common}`", str(common_n)])

    lines = [
        "## Mechanical merge candidates",
        "",
        "Derived by rule, not judgement - every pair here is a spelling of the "
        "same idea. Nothing has been renamed; `tags/rename` runs only after "
        "you approve.",
        "",
    ]
    if rows:
        lines += _table(["fold this", "uses", "into", "uses"], rows)
    else:
        lines += ["None.", ""]
    return lines


def render(stats: Stats, backlog: dict[str, Any], generated: str) -> str:
    """The full analysis document."""
    parts: list[str] = [
        "# Pinboard archive analysis",
        "",
        f"Generated {generated} from `data/pins_raw.json`.",
        "",
        *_overview(stats),
        *_cadence(stats),
        *_hygiene(stats),
        *_frequency(stats),
        *_duplicates(stats),
        *_clusters(stats),
        *_domains(stats),
        *_backlog(backlog),
        *_style(stats),
        *_merges(stats),
        CURATED_MARKER,
        "",
    ]
    return "\n".join(parts)


def merge_curated(fresh: str, existing: str | None) -> str:
    """Keep anything hand-written below the curated marker across re-runs."""
    if not existing or CURATED_MARKER not in existing:
        return fresh
    tail = existing.split(CURATED_MARKER, 1)[1]
    return fresh.split(CURATED_MARKER, 1)[0] + CURATED_MARKER + tail


def stats_payload(stats: Stats, backlog: dict[str, Any]) -> dict[str, Any]:
    """A machine-readable digest, handy for the skill and for diffing runs."""
    counts: Counter[str] = stats.counts
    return {
        "total_pins": stats.total,
        "untagged": len(stats.untagged),
        "single_tag": len(stats.single_tag),
        "distinct_tags": len(counts),
        "tag_counts": dict(counts.most_common()),
        "months": stats.months,
        "domains": dict(stats.domains.most_common(TOP_DOMAINS)),
        "toread": backlog,
        "tags_per_year": tags_per_year(stats.pins),
        "variant_groups": [
            {"key": g.key, "kinds": g.kinds, "members": g.members}
            for g in variant_groups(dict(counts))
        ],
        "typo_candidates": typo_candidates(dict(counts)),
    }
