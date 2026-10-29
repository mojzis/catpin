"""Area inference, and the neutral set that keeps it honest."""

from catpin.areas import (
    AMBIGUOUS,
    NO_SIGNAL,
    UNTAGGED,
    classify,
    classify_pin,
    load_seeds,
)

RAW = {
    "_comment": "ignored",
    "_neutral": ["book"],
    "work": ["data", "python"],
    "family": ["kids", "trip"],
}
SEEDS, NEUTRAL = load_seeds(RAW)


def pin(tags: str) -> dict[str, str]:
    """A pin carrying just the tags under test."""
    return {
        "tags": tags,
        "href": "https://example.test/a",
        "time": "2024-01-01T00:00:00Z",
    }


def test_load_seeds_separates_the_neutral_set():
    assert {"book"} == NEUTRAL
    assert set(SEEDS) == {"work", "family"}


def test_a_pin_with_one_area_tag_is_assigned_to_it():
    assert classify_pin(pin("python"), SEEDS, NEUTRAL) == "work"


def test_the_area_with_more_matching_tags_wins():
    assert classify_pin(pin("python data kids"), SEEDS, NEUTRAL) == "work"


def test_an_even_split_is_ambiguous():
    assert classify_pin(pin("python kids"), SEEDS, NEUTRAL) == AMBIGUOUS


def test_a_neutral_tag_never_decides_an_area():
    assert classify_pin(pin("book"), SEEDS, NEUTRAL) == NO_SIGNAL


def test_a_neutral_tag_does_not_manufacture_ambiguity():
    assert classify_pin(pin("python book"), SEEDS, NEUTRAL) == "work"


def test_a_tagged_pin_with_no_seed_tag_has_no_signal():
    assert classify_pin(pin("obscure"), SEEDS, NEUTRAL) == NO_SIGNAL


def test_an_untagged_pin_is_reported_as_untagged():
    assert classify_pin(pin(""), SEEDS, NEUTRAL) == UNTAGGED


def test_classify_collects_the_ambiguous_pins():
    result = classify([pin("python"), pin("python kids")], SEEDS, NEUTRAL)
    assert result.counts["work"] == 1
    assert len(result.ambiguous) == 1


def test_share_is_a_percentage_of_all_classified_pins():
    result = classify(
        [pin("python"), pin("kids"), pin("kids"), pin("")], SEEDS, NEUTRAL
    )
    assert result.share("family") == 50.0
