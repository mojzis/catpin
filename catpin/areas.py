"""Guessing the area of life a pin belongs to, from its tags.

The seeds are a hypothesis kept in ``areas.json``, not a fact. Type and
dual-use tags are excluded: a ``book`` can be work or family, and leaving
such tags in the seeds manufactures ambiguity rather than finding it.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from .analysis import Pin, pin_tags

Seeds = dict[str, set[str]]


def load_seeds(raw: dict[str, Any]) -> tuple[Seeds, set[str]]:
    """Split an ``areas.json`` mapping into seed sets and the neutral set."""
    neutral = {str(t) for t in raw.get("_neutral", [])}
    seeds = {
        name: {str(t) for t in tags}
        for name, tags in raw.items()
        if not name.startswith("_") and isinstance(tags, list)
    }
    return seeds, neutral


UNTAGGED = "untagged"
NO_SIGNAL = "no area signal"
AMBIGUOUS = "ambiguous"


def classify_pin(pin: Pin, seeds: Seeds, neutral: set[str]) -> str:
    """The area a single pin lands in, or why it could not be decided."""
    tags = set(pin_tags(pin))
    if not tags:
        return UNTAGGED
    scores = {name: len(tags & seed - neutral) for name, seed in seeds.items()}
    best = max(scores.values(), default=0)
    if not best:
        return NO_SIGNAL
    winners = [name for name, score in scores.items() if score == best]
    return winners[0] if len(winners) == 1 else AMBIGUOUS


@dataclass
class AreaResult:
    """Per-area counts plus the pins that could not be decided."""

    counts: Counter[str] = field(default_factory=Counter)
    ambiguous: list[Pin] = field(default_factory=list)

    @property
    def total(self) -> int:
        """Pins classified."""
        return sum(self.counts.values())

    def share(self, label: str) -> float:
        """Percentage of the archive in one bucket."""
        return round(100 * self.counts[label] / self.total, 1) if self.total else 0.0


def classify(pins: list[Pin], seeds: Seeds, neutral: set[str]) -> AreaResult:
    """Assign every pin to an area, collecting the undecidable ones."""
    result = AreaResult()
    for pin in pins:
        label = classify_pin(pin, seeds, neutral)
        result.counts[label] += 1
        if label == AMBIGUOUS:
            result.ambiguous.append(pin)
    return result
