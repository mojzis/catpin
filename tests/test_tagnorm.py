"""Normalisation must fold the four ways a tag gets rewritten by hand."""

from catpin.tagnorm import (
    edit_distance,
    normalize,
    singular,
    typo_candidates,
    variant_groups,
)


def test_normalize_folds_case_separators_and_camel_case():
    keys = {
        normalize(t) for t in ["python-dev", "python_dev", "pythonDev", "Python Dev"]
    }
    assert keys == {"python dev"}


def test_normalize_folds_plurals():
    assert normalize("papers") == normalize("paper")


def test_singular_leaves_short_and_double_s_words_alone():
    assert singular("css") == "css"
    assert singular("gas") == "gas"


def test_variant_groups_ranks_the_most_used_spelling_first():
    groups = variant_groups({"python": 40, "Python": 10, "PYTHON": 2})
    assert groups[0].winner == "python"
    assert groups[0].total == 52


def test_variant_groups_names_the_kind_of_difference():
    groups = variant_groups({"python-dev": 3, "pythonDev": 1})
    assert groups[0].kinds == ["separator"]


def test_variant_groups_ignores_tags_with_no_twin():
    assert variant_groups({"python": 40, "energy": 9}) == []


def test_edit_distance_stops_counting_past_the_limit():
    assert edit_distance("abcdef", "uvwxyz", limit=2) == 3


def test_typo_candidates_points_the_rare_spelling_at_the_common_one():
    assert typo_candidates({"kubernetes": 12, "kubernets": 1}) == [
        ("kubernets", "kubernetes", 1, 12)
    ]


def test_typo_candidates_ignores_two_similarly_common_tags():
    assert typo_candidates({"kubernetes": 12, "kubernets": 11}) == []


def test_variant_groups_prefer_lowercase_when_counts_tie():
    assert variant_groups({"Python": 5, "python": 5})[0].winner == "python"
