"""The local cleanup rewrites a copy and leaves the raw archive alone."""

from catpin.clean import clean_pins, rewrite_tags

MAPPING = {"tools": "tool", "Security": "security", "travel": "trip"}


def test_rewrite_tags_folds_through_the_mapping():
    folded, _ = rewrite_tags(["tools", "python"], MAPPING)
    assert folded == ["tool", "python"]


def test_rewrite_tags_collapses_a_duplicate_the_fold_creates():
    folded, collapsed = rewrite_tags(["tool", "tools"], MAPPING)
    assert folded == ["tool"]
    assert collapsed == 1


def test_rewrite_tags_keeps_the_original_order():
    folded, _ = rewrite_tags(["python", "tools", "data"], MAPPING)
    assert folded == ["python", "tool", "data"]


def test_rewrite_tags_leaves_unmapped_tags_untouched():
    folded, collapsed = rewrite_tags(["python", "data"], MAPPING)
    assert folded == ["python", "data"]
    assert collapsed == 0


def test_clean_pins_does_not_mutate_the_input(pins):
    before = [p["tags"] for p in pins]
    clean_pins(pins, MAPPING)
    assert [p["tags"] for p in pins] == before


def test_clean_pins_reports_the_tag_count_it_removed(pins):
    result = clean_pins(pins, {"Python": "python"})
    assert result.tags_before == 10
    assert result.tags_after == 9


def test_clean_pins_counts_pins_touched_per_fold(pins):
    result = clean_pins(pins, {"Python": "python"})
    assert result.applied["Python -> python"] == 1


def test_clean_pins_preserves_every_other_field(pins):
    cleaned = clean_pins(pins, MAPPING).pins
    assert cleaned[0]["href"] == pins[0]["href"]
    assert cleaned[0]["toread"] == pins[0]["toread"]


def test_clean_pins_keeps_untagged_pins_untagged(pins):
    cleaned = clean_pins(pins, MAPPING).pins
    assert cleaned[2]["tags"] == ""
