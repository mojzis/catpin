# Findings

Archive of 2126 pins, 2017-07 to 2026-09. Numbers from `data/analysis.md`
(regenerate with `pins.py analyse`). Nothing has been written to Pinboard.

## 1. The tagging habit is collapsing

| year | pins | tags/pin | untagged |
|---|---|---|---|
| 2020 | 377 | 1.29 | 7% |
| 2023 | 275 | 0.95 | 23% |
| 2024 | 226 | **0.38** | **67%** |
| 2025 | 296 | 0.87 | 31% |
| 2026 | 143 | **0.19** | **85%** |

Archive-wide: 28% untagged, 51% exactly one tag, 20% two or more.

The 600 untagged pins are **not** a hidden category - their domains mirror the
archive (github 66, theguardian 30, the two top domains overall). They are just
recent. Untagged tracks the habit, nothing else.

Pinning itself is healthy: 111 months, no empty month. Peak Dec 2020 (123).

## 2. Facets that exist

Top 30 tags: **24 topic, 4 type, 1 status, 2 ambiguous.**

| facet | uses | share | state |
|---|---|---|---|
| topic | ~1810 | 89% | works, unambiguous |
| type | ~195 | 9.6% | thin - `book` 69 is most of it |
| status | 49 | 2.4% | effectively absent (`job` 34 is nearly all) |
| aspect | ~80 | 4% | used consistently, never named |

**aspect** = `performance` 39, `security` 21, `testing` 13, `privacy`,
`validation`, `ethics`. Cross-cutting qualities, not subjects. Worth naming.

Missing: type absent from ~90% of pins (207 github pins, 36 `tool` uses); no
language facet though ~1 pin in 7 is Czech; `toread` flag dormant since 2020
(39 pins, median age 8.9 years, 28 untagged).

**Not proposed:** a status facet to fill in going forward. Never used, and with
half the pins on one tag it would mostly produce blanks.

## 3. Areas of life

`pins.py area`, seeds in `areas.json`.

| | pins | share |
|---|---|---|
| work | 690 | 32.5% |
| family | 367 | 17.3% |
| hunt | 32 | 1.5% |
| no area signal | 417 | 19.6% |
| untagged | 600 | 28.2% |
| **ambiguous** | **20** | **0.9%** |

Area is a learnable signal. Ambiguity was 46 (2.2%) until type and dual-use
tags were moved to `_neutral` - `book`, `image`, `raspberrypi` caused 19 of
those 46. A `book` can be work or family; type and area are orthogonal.

## 4. Hunts are a shape, not a vocabulary

Seeding `hunt` from tags found 1.5%, far below intuition. A hunt does not reuse
vocabulary: it invents a throwaway tag, uses it twice in one afternoon, never
returns. Look at timing. `pins.py burst`.

**33 of 502 tags have every pin inside 60 days**, most inside one day:

| tag | pins | span | what |
|---|---|---|---|
| `lipno` | 6 | 0d | booking a cabin |
| `svata` `tuber` `koleda` | 4 | 0d | Dec 2020 |
| `sicily` | 3 | 0d | trip planning |
| `gympl` | 2 | 0d | choosing a high school |
| `maringotka` | 2 | 0d | buying a caravan |
| `mia` | 2 | 0d | water tank and pump |
| `kroužky` | 2 | 0d | ornithology clubs |

Opposite end: `testing` 3261d, `tool` 3091d, `trip` 3078d, `kids` 2908d.

Bursts are **two** things with one shape. A **hunt** seeks a decision (`lipno`,
`gympl`, `maringotka`). A **binge** seeks a subject - `underground`, `koleda`,
`svata`, `gospel`, `christmas`, `tuber`, all December 2020, one dive into Czech
music. Timing separates bursts from standing interests; only content separates
hunt from binge.

## 5. `data` is a folder name

| | `data` | `trip` |
|---|---|---|
| pins | 121 | 82 |
| sole tag on | **60 (50%)** | - |
| top partner | `visualization` 10 | `nature` 4 |

On half its pins `data` is the only tag, so it carries everything and
distinguishes nothing. It covers ~18% of the work domain. `trip` is the
contrast: it maps to an area *and* stays specific inside it; `data` maps to an
area and then *is* the area.

The sub-vocabulary already exists and is bypassed: `metadata` 9, `reporting` 9,
`analytics` 9, `datavault` 8, `dwh` 4, `modelling` 4. A keyword pass over the 60
sole-`data` pins reaches **24 (40%)**:

| would take | pins | exists today |
|---|---|---|
| pipelines | 7 | **0 - missing tag** |
| governance | 5 | 1 |
| book | 4 | 69 |
| management / analytics / modelling | 8 | 8 / 9 / 4 |
| no keyword match | 36 | |

`pipelines` is a missing tag justified by evidence. The other 36 - "Positron",
"intake/intake", "Wes McKinney - Composable Data Systems" - cannot be reached
from the title. **Backfill needs the page, not the title.**

## 6. Why not prefix topics by group (`ai:llm`)

A prefix forces single parenthood and these tags have two parents - exactly what
produced the 19 false ambiguities above. `raspberrypi` is work at the office and
hobby at home. Grouping is better as a *view* (a mapping in this repo, wrong for
free) than as storage (a rename, permanent). Topic is also the facet that
already works, so the worst place to spend a migration.

## 7. Method notes

- **Pinboard folds case itself.** `tags/get` reports `security: 22` = 21
  `security` + 1 `Security`; same for all six pairs. Case never mattered for
  search. It matters locally only, because `posts/all` returns stored per-pin
  case. Hence the local-only `case` group.
- **Both edit-distance folds were wrong.** `corse` is Corsica, `nodes` is graph
  nodes. A rule-based pass matches spelling without meaning. Use
  `pins.py show <tag>` before adding any fold.
- **Cleaning changes what the analysis can see.** Folding `note-taking` into
  `notes` lifted it 2 -> 4 uses and made `nodes` cross the typo threshold. Re-run
  `analyse` after `clean`. Second pass converged.
- **Clean locally first.** `clean` is reversible, `tags/rename` is not.

## 8. Open

- `kroužky` (2) - left unfolded, reads as a hunt like `gympl`.
- `sucho` (3) - left out of `climate`; drought is narrower.
- `clarity` group held back (`lily`->`lilypond`, `vault`->`datavault`,
  `stars`->`astronomy`). Run `clean -g clarity` to try it.
- Whether the tagger should propose **type** and **aspect** tags, or topic only.
  Type is the weakest facet, so the highest-value change - but it is a change.

## 9. Next: content analysis

Backfill 600 untagged + 1091 single-tag pins. Constraints found above:

1. Titles are not enough - 60% of the `data` cases need the page. Only 21 of the
   600 untagged pins have an `extended` note.
2. Constrain to the 86-tag core vocabulary (69% of use); flag anything new.
3. Assign **area** in the same pass as topic. Backfill is ~600 `posts/add` calls
   at 1/s and each rewrites a live pin; do not pay that twice.
4. `posts/add` with `replace=yes` must resend `description`, `extended`, `dt`,
   `shared`, `toread` or they are cleared.

Interface for an external tagger: `(url, title, extended, domain) -> tags`.
