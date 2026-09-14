"""Statistics over the synthetic archive."""

from datetime import UTC, datetime

from catpin.analysis import (
    Stats,
    cooccurrence,
    month_range,
    neighbours,
    per_month,
    pin_domain,
    pin_tags,
    quiet_runs,
    tags_per_year,
    toread_backlog,
)

NOW = datetime(2023, 3, 1, tzinfo=UTC)


def test_pin_tags_splits_the_space_separated_string(pins):
    assert pin_tags(pins[0]) == ["python", "tool"]


def test_pin_tags_of_an_untagged_pin_is_empty(pins):
    assert pin_tags(pins[2]) == []


def test_pin_domain_drops_the_www_prefix(pins):
    assert pin_domain(pins[0]) == "github.com"


def test_month_range_crosses_the_year_boundary():
    assert month_range("2021-11", "2022-02") == [
        "2021-11",
        "2021-12",
        "2022-01",
        "2022-02",
    ]


def test_per_month_keeps_empty_months_as_zero(pins):
    months = per_month(pins)
    assert months["2021-02"] == 0
    assert months["2021-01"] == 2


def test_quiet_runs_reports_the_longest_gap_first(pins):
    longest = quiet_runs(per_month(pins))[0]
    assert longest == ("2021-04", "2022-05", 14)


def test_untagged_and_single_tag_are_counted_separately(pins):
    stats = Stats(pins=pins, now=NOW)
    assert len(stats.untagged) == 1
    assert len(stats.single_tag) == 3


def test_action_only_pins_carry_no_subject_tag(pins):
    stats = Stats(pins=pins, now=NOW)
    assert [pin_tags(p) for p in stats.action_only] == [["toread"]]


def test_domains_are_counted_across_the_archive(pins):
    assert Stats(pins=pins, now=NOW).domains["github.com"] == 3


def test_cooccurrence_counts_unordered_pairs(pins):
    pairs = cooccurrence(pins, min_pair=1)
    assert pairs[("python", "tool")] == 1
    assert pairs[("energy", "grid")] == 1


def test_neighbours_ranks_by_similarity(pins):
    stats = Stats(pins=pins, now=NOW)
    pairs = cooccurrence(pins, min_pair=1)
    assert neighbours(pairs, stats.counts, "energy")[0][0] == "grid"


def test_tags_per_year_tracks_the_untagged_share(pins):
    yearly = tags_per_year(pins)
    assert yearly[2021]["untagged_pct"] == 33.3
    assert yearly[2023]["mean_tags"] == 2.0


def test_toread_backlog_reports_size_and_oldest_age(pins):
    backlog = toread_backlog(pins, NOW)
    assert backlog["count"] == 3
    assert backlog["oldest_age_days"] == 261
