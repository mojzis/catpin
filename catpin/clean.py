"""Apply a rename plan to a cached archive, in memory.

This is the local half of the cleanup: the raw cache is never modified, and
Pinboard is never contacted. It exists so that analysis can run against the
vocabulary you are *considering* before you commit to it.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Any

Pin = dict[str, Any]


@dataclass
class CleanResult:
    """The rewritten pins, plus enough detail to see what the plan did."""

    pins: list[Pin]
    applied: Counter[str] = field(default_factory=Counter)
    collapsed: int = 0
    tags_before: int = 0
    tags_after: int = 0

    @property
    def pins_changed(self) -> int:
        """How many pins had at least one tag rewritten."""
        return sum(self.applied.values())

    @property
    def unused(self) -> list[str]:
        """Folds in the plan that matched nothing in this archive."""
        return sorted(self.applied)


def rewrite_tags(tags: list[str], mapping: dict[str, str]) -> tuple[list[str], int]:
    """Fold ``tags`` through ``mapping``, dropping duplicates it creates.

    Returns the new tag list and the number of duplicates collapsed, which is
    the interesting part: a pin tagged both ``tool`` and ``tools`` ends up with
    one tag, not two identical ones.
    """
    seen: dict[str, None] = {}
    for tag in tags:
        seen.setdefault(mapping.get(tag, tag), None)
    folded = list(seen)
    return folded, len(tags) - len(folded)


def clean_pins(pins: list[Pin], mapping: dict[str, str]) -> CleanResult:
    """Return a copy of ``pins`` with the rename plan applied to every tag."""
    before: Counter[str] = Counter()
    after: Counter[str] = Counter()
    result = CleanResult(pins=[])

    for pin in pins:
        tags = str(pin.get("tags", "")).split()
        before.update(tags)
        folded, collapsed = rewrite_tags(tags, mapping)
        after.update(folded)
        result.collapsed += collapsed

        if folded != tags:
            for tag in tags:
                if tag in mapping:
                    result.applied[f"{tag} -> {mapping[tag]}"] += 1

        result.pins.append({**pin, "tags": " ".join(folded)})

    result.tags_before = len(before)
    result.tags_after = len(after)
    return result
