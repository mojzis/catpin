"""Statistics over a Pinboard archive.

Everything here is pure: it takes the list of pin dicts as Pinboard returns
them from ``posts/all`` and returns plain data. No network, no files.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from itertools import combinations
from typing import Any
from urllib.parse import urlsplit

Pin = dict[str, Any]

#: Tags carrying workflow meaning rather than subject meaning.
ACTION_TAGS = frozenset({"toread", "reference", "try", "read", "later", "todo"})

_DECEMBER = 12
_MONTH_DAYS = 30
_YEAR_DAYS = 365
_OLD_YEARS = 3


def pin_time(pin: Pin) -> datetime:
    """The pin's creation instant, as an aware UTC datetime."""
    raw = str(pin.get("time", "")).replace("Z", "+00:00")
    return datetime.fromisoformat(raw).astimezone(UTC)


def pin_tags(pin: Pin) -> list[str]:
    """The pin's tags. Pinboard returns them space-separated in JSON."""
    raw = pin.get("tags", "")
    if isinstance(raw, list):
        return [str(t) for t in raw if str(t).strip()]
    return str(raw).split()


def pin_domain(pin: Pin) -> str:
    """Registered host of the pinned URL, without a ``www.`` prefix."""
    host = urlsplit(str(pin.get("href", ""))).netloc.lower()
    host = host.split("@")[-1].split(":")[0]
    return host.removeprefix("www.")


def month_key(moment: datetime) -> str:
    """``YYYY-MM`` bucket label."""
    return f"{moment.year:04d}-{moment.month:02d}"


def month_range(first: str, last: str) -> list[str]:
    """Every ``YYYY-MM`` from ``first`` to ``last`` inclusive, gaps included."""
    year, month = (int(part) for part in first.split("-"))
    end_year, end_month = (int(part) for part in last.split("-"))
    months = []
    while (year, month) <= (end_year, end_month):
        months.append(f"{year:04d}-{month:02d}")
        year, month = (year + 1, 1) if month == _DECEMBER else (year, month + 1)
    return months


def per_month(pins: list[Pin]) -> dict[str, int]:
    """Pins created per month, with empty months present as zero."""
    counts = Counter(month_key(pin_time(p)) for p in pins)
    if not counts:
        return {}
    span = month_range(min(counts), max(counts))
    return {month: counts.get(month, 0) for month in span}


def quiet_runs(
    months: dict[str, int], min_length: int = 2
) -> list[tuple[str, str, int]]:
    """Stretches of consecutive months with no pins at all."""
    runs: list[tuple[str, str, int]] = []
    start: str | None = None
    previous: str | None = None
    for month, count in months.items():
        if count == 0:
            start = start or month
            previous = month
        elif start and previous:
            runs.append((start, previous, len(month_range(start, previous))))
            start = previous = None
    if start and previous:
        runs.append((start, previous, len(month_range(start, previous))))
    return sorted((r for r in runs if r[2] >= min_length), key=lambda r: -r[2])


def tag_counts(pins: list[Pin]) -> Counter[str]:
    """How often each tag is used across the archive."""
    return Counter(tag for pin in pins for tag in pin_tags(pin))


def tags_per_year(pins: list[Pin]) -> dict[int, dict[str, float]]:
    """Per year: pin count, mean tags per pin, and the untagged share."""
    buckets: dict[int, list[int]] = defaultdict(list)
    for pin in pins:
        buckets[pin_time(pin).year].append(len(pin_tags(pin)))
    summary = {}
    for year in sorted(buckets):
        sizes = buckets[year]
        summary[year] = {
            "pins": float(len(sizes)),
            "mean_tags": round(sum(sizes) / len(sizes), 2),
            "untagged_pct": round(
                100 * sum(1 for s in sizes if s == 0) / len(sizes), 1
            ),
            "single_tag_pct": round(
                100 * sum(1 for s in sizes if s == 1) / len(sizes), 1
            ),
        }
    return summary


def cooccurrence(pins: list[Pin], min_pair: int = 3) -> Counter[tuple[str, str]]:
    """How often each unordered tag pair appears on the same pin."""
    pairs: Counter[tuple[str, str]] = Counter()
    for pin in pins:
        tags = sorted(set(pin_tags(pin)))
        pairs.update(combinations(tags, 2))
    return Counter({pair: n for pair, n in pairs.items() if n >= min_pair})


def neighbours(
    pairs: Counter[tuple[str, str]],
    counts: Counter[str],
    tag: str,
    limit: int = 5,
) -> list[tuple[str, int, float]]:
    """The tags that travel with ``tag``, ranked by Jaccard similarity."""
    found = []
    for (left, right), shared in pairs.items():
        if tag not in (left, right):
            continue
        other = right if left == tag else left
        union = counts[tag] + counts[other] - shared
        if union:
            found.append((other, shared, round(shared / union, 3)))
    return sorted(found, key=lambda n: (-n[2], -n[1]))[:limit]


def toread_backlog(pins: list[Pin], now: datetime) -> dict[str, Any]:
    """Size and age profile of the unread pile."""
    unread = [p for p in pins if str(p.get("toread", "no")) == "yes"]
    ages = sorted((now - pin_time(p)).days for p in unread)
    buckets = Counter()
    for days in ages:
        if days < _MONTH_DAYS:
            buckets["under 1 month"] += 1
        elif days < _YEAR_DAYS:
            buckets["1-12 months"] += 1
        elif days < _YEAR_DAYS * _OLD_YEARS:
            buckets["1-3 years"] += 1
        else:
            buckets["over 3 years"] += 1
    return {
        "count": len(unread),
        "share_pct": round(100 * len(unread) / len(pins), 1) if pins else 0.0,
        "median_age_days": ages[len(ages) // 2] if ages else 0,
        "oldest_age_days": ages[-1] if ages else 0,
        "age_buckets": dict(buckets),
        "untagged": sum(1 for p in unread if not pin_tags(p)),
    }


@dataclass
class Stats:
    """Everything the report needs, computed once."""

    pins: list[Pin]
    now: datetime

    @property
    def total(self) -> int:
        """Number of pins in the archive."""
        return len(self.pins)

    @property
    def counts(self) -> Counter[str]:
        """Tag use counts."""
        return tag_counts(self.pins)

    @property
    def untagged(self) -> list[Pin]:
        """Pins carrying no tags at all."""
        return [p for p in self.pins if not pin_tags(p)]

    @property
    def single_tag(self) -> list[Pin]:
        """Pins carrying exactly one tag."""
        return [p for p in self.pins if len(pin_tags(p)) == 1]

    @property
    def action_only(self) -> list[Pin]:
        """Pins whose only tags are workflow markers, so subject-less."""
        return [p for p in self.pins if pin_tags(p) and set(pin_tags(p)) <= ACTION_TAGS]

    @property
    def domains(self) -> Counter[str]:
        """Pins per host."""
        return Counter(pin_domain(p) for p in self.pins if pin_domain(p))

    @property
    def months(self) -> dict[str, int]:
        """Pins per month across the whole history."""
        return per_month(self.pins)


def tag_span(pins: list[Pin], tag: str) -> tuple[int, str, str]:
    """Days from the first to the last pin carrying ``tag``, and the endpoints.

    A short span on a rarely-used tag is the signature of a burst: a hunt or a
    binge that invented a tag, used it over an afternoon and never came back.
    """
    times = sorted(pin_time(p) for p in pins if tag in pin_tags(p))
    if not times:
        return (0, "-", "-")
    first, last = times[0], times[-1]
    return ((last - first).days, month_key(first), month_key(last))
