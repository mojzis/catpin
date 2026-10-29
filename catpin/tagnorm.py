"""Tag normalisation and near-duplicate detection.

Two tags are *variants* of each other when they collapse to the same
comparison key after folding case, separators, camelCase humps and simple
English/Czech plural endings. Anything the key misses is caught by a
conservative edit-distance pass.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field

_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_NON_ALNUM = re.compile(r"[^0-9a-zA-Z]+")

#: Below this length an edit of one character is usually a different word.
MIN_TYPO_LEN = 5
#: A rare tag one edit away from a common one is suspected to be a typo.
TYPO_RATIO = 4

_SHORT_WORD = 4
_TINY_WORD = 3
_PAIR = 2


def split_words(tag: str) -> list[str]:
    """Break a tag into lowercase words across case and separator changes."""
    spaced = _CAMEL.sub(" ", tag)
    return _NON_ALNUM.sub(" ", spaced).lower().split()


def singular(word: str) -> str:
    """Strip the common plural endings shared by English and Czech tags."""
    if len(word) > _SHORT_WORD and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > _SHORT_WORD and word.endswith(("ses", "xes", "zes", "ches", "shes")):
        return word[:-2]
    if len(word) > _TINY_WORD and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def normalize(tag: str) -> str:
    """Comparison key that ignores case, separators and plurals."""
    return " ".join(singular(word) for word in split_words(tag))


def _difference_kinds(tags: list[str]) -> list[str]:
    """Name the ways a set of same-key tags differ from one another."""
    kinds: list[str] = []
    if len({t.lower() for t in tags}) < len(tags):
        kinds.append("case")
    separators = {tuple(_NON_ALNUM.findall(t)) for t in tags}
    humps = {bool(_CAMEL.search(t)) for t in tags}
    if len(separators) > 1 or len(humps) > 1:
        kinds.append("separator")
    if len({" ".join(split_words(t)) for t in tags}) > 1:
        kinds.append("plural")
    return kinds or ["spelling"]


def _preference(tag: str, count: int) -> tuple[int, bool, int, str]:
    """Rank a spelling: most used, then lowercase, then shortest."""
    return (-count, tag != tag.lower(), len(tag), tag)


@dataclass
class VariantGroup:
    """A set of tags that mean the same thing, and why they differ."""

    key: str
    members: list[tuple[str, int]] = field(default_factory=list)
    kinds: list[str] = field(default_factory=list)

    @property
    def total(self) -> int:
        """Combined use count across every member."""
        return sum(count for _, count in self.members)

    @property
    def winner(self) -> str:
        """The most-used member, which is the natural merge target."""
        return self.members[0][0]


def variant_groups(counts: dict[str, int]) -> list[VariantGroup]:
    """Group tags that share a normalised key, most-used member first."""
    buckets: dict[str, list[str]] = defaultdict(list)
    for tag in counts:
        buckets[normalize(tag)].append(tag)

    groups = []
    for key, tags in buckets.items():
        if len(tags) < _PAIR:
            continue
        members = sorted(tags, key=lambda t: _preference(t, counts[t]))
        groups.append(
            VariantGroup(
                key=key,
                members=[(t, counts[t]) for t in members],
                kinds=_difference_kinds(members),
            )
        )
    return sorted(groups, key=lambda g: -g.total)


def edit_distance(a: str, b: str, limit: int = 2) -> int:
    """Levenshtein distance, giving up once it is known to exceed ``limit``."""
    if abs(len(a) - len(b)) > limit:
        return limit + 1
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        current = [i]
        for j, cb in enumerate(b, start=1):
            current.append(
                min(
                    previous[j] + 1,
                    current[j - 1] + 1,
                    previous[j - 1] + (ca != cb),
                )
            )
        if min(current) > limit:
            return limit + 1
        previous = current
    return previous[-1]


def typo_candidates(counts: dict[str, int]) -> list[tuple[str, str, int, int]]:
    """Rare tags one edit away from a much more common tag.

    Returns ``(rare, common, rare_count, common_count)`` tuples, skipping
    pairs that :func:`variant_groups` already reports.
    """
    tags = [t for t in counts if len(t) >= MIN_TYPO_LEN]
    ranked = sorted(tags, key=lambda t: -counts[t])
    found = []
    for i, common in enumerate(ranked):
        for rare in ranked[i + 1 :]:
            if counts[common] < counts[rare] * TYPO_RATIO:
                continue
            if normalize(common) == normalize(rare):
                continue
            if common[0] != rare[0]:
                continue
            if edit_distance(common.lower(), rare.lower(), limit=1) == 1:
                found.append((rare, common, counts[rare], counts[common]))
    return sorted(found, key=lambda pair: -pair[3])
