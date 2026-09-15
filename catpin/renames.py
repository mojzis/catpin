"""Loading and validating a tag rename plan.

A plan is a mapping of groups to ``{old: new}`` pairs. Validation is the
interesting part: a chain (``a -> b`` while ``b -> c``) makes the outcome
depend on execution order, so it is refused rather than guessed at.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

#: A plan as read from JSON: group name -> {old: new}, plus "_"-prefixed
#: comment keys holding anything at all.
Plan = Mapping[str, object]


class RenamePlanError(ValueError):
    """The rename plan cannot be applied as written."""


class ChainedRenameError(RenamePlanError):
    """A tag is both a source and a target, so the result depends on order."""

    def __init__(self, chained: list[str]) -> None:
        super().__init__(f"chained renames, order-dependent: {', '.join(chained)}")
        self.chained = chained


class DuplicateSourceError(RenamePlanError):
    """The same tag is renamed twice, to different targets."""

    def __init__(self, duplicates: list[str]) -> None:
        super().__init__(f"tag renamed more than once: {', '.join(duplicates)}")
        self.duplicates = duplicates


@dataclass
class Rename:
    """One rename, with the use counts that make its effect readable."""

    old: str
    new: str
    group: str
    old_uses: int
    new_uses: int

    @property
    def exists(self) -> bool:
        """Whether the source tag is actually present in the account."""
        return self.old_uses > 0

    @property
    def merges(self) -> bool:
        """Whether the target already exists, making this a merge."""
        return self.new_uses > 0

    @property
    def result_uses(self) -> int:
        """Uses the target carries once this rename is applied."""
        return self.old_uses + self.new_uses


def groups_of(plan: Plan) -> dict[str, dict[str, str]]:
    """The rename groups, skipping comment keys and any non-mapping entry."""
    return {
        name: {str(old): str(new) for old, new in value.items()}
        for name, value in plan.items()
        if not name.startswith("_") and isinstance(value, dict)
    }


def select(plan: Plan, groups: list[str] | None = None) -> dict[str, str]:
    """Flatten the chosen groups into one ``{old: new}`` mapping."""
    available = groups_of(plan)
    chosen = [g for g in available if not groups or g in groups]

    flat: dict[str, str] = {}
    duplicates = []
    for group in chosen:
        for old, new in available[group].items():
            if old in flat and flat[old] != new:
                duplicates.append(old)
            flat[old] = new
    if duplicates:
        raise DuplicateSourceError(sorted(set(duplicates)))
    return flat


def validate(mapping: dict[str, str]) -> None:
    """Refuse a mapping whose result would depend on execution order."""
    chained = sorted(set(mapping) & set(mapping.values()))
    if chained:
        raise ChainedRenameError(chained)


def plan_renames(
    plan: Plan,
    counts: dict[str, int],
    groups: list[str] | None = None,
) -> list[Rename]:
    """Resolve a plan against live tag counts, most-used source first."""
    mapping = select(plan, groups)
    validate(mapping)

    group_of = {old: group for group, pairs in groups_of(plan).items() for old in pairs}
    renames = [
        Rename(
            old=old,
            new=new,
            group=group_of.get(old, "?"),
            old_uses=counts.get(old, 0),
            new_uses=counts.get(new, 0),
        )
        for old, new in mapping.items()
    ]
    return sorted(renames, key=lambda r: (-r.old_uses, r.old))
