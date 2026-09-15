"""A rename plan must be refused rather than guessed at when it is ambiguous."""

import pytest

from catpin.renames import (
    ChainedRenameError,
    DuplicateSourceError,
    plan_renames,
    select,
    validate,
)

PLAN = {
    "_comment": "ignored",
    "safe": {"tools": "tool", "charts": "chart"},
    "semantic": {"travel": "trip"},
}
COUNTS = {"tools": 20, "tool": 16, "charts": 2, "chart": 13, "travel": 9, "trip": 73}


def test_select_skips_underscore_prefixed_keys():
    assert "_comment" not in select(PLAN)


def test_select_can_narrow_to_one_group():
    assert select(PLAN, ["semantic"]) == {"travel": "trip"}


def test_select_refuses_a_tag_renamed_to_two_targets():
    plan = {"a": {"x": "y"}, "b": {"x": "z"}}
    with pytest.raises(DuplicateSourceError):
        select(plan)


def test_validate_refuses_an_order_dependent_chain():
    with pytest.raises(ChainedRenameError):
        validate({"a": "b", "b": "c"})


def test_two_tags_may_fold_into_the_same_target():
    plan = {"safe": {"tools": "tool", "gear": "tool"}}
    assert [r.new for r in plan_renames(plan, COUNTS)] == ["tool", "tool"]


def test_plan_renames_orders_by_the_uses_at_stake():
    assert [r.old for r in plan_renames(PLAN, COUNTS)] == ["tools", "travel", "charts"]


def test_plan_renames_reports_the_combined_result():
    tools = plan_renames(PLAN, COUNTS)[0]
    assert tools.merges
    assert tools.result_uses == 36


def test_a_source_absent_from_the_counts_is_marked_as_such():
    absent = plan_renames({"safe": {"ghost": "tool"}}, COUNTS)[0]
    assert not absent.exists


def test_renaming_to_a_new_name_is_not_a_merge():
    fresh = plan_renames({"clarity": {"tools": "gear"}}, COUNTS)[0]
    assert not fresh.merges
    assert fresh.result_uses == 20
