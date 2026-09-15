# Pinboard archive analysis

Generated 2026-09-15 from `data/pins_raw.json`.

## Overview

| metric | value |
|---|---|
| pins | 2126 |
| first month | 2017-07 |
| last month | 2026-09 |
| months spanned | 111 |
| months with at least one pin | 111 |
| mean pins / active month | 19.2 |
| distinct tags | 502 |
| distinct domains | 1298 |

Busiest months: 2020-12 (123), 2020-11 (90), 2021-01 (60), 2025-06 (50), 2025-05 (41).

## Cadence

Pins per month over the whole history (`.` is a month with no pins).

| year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | . | . | . | . | . | . | 7 | 20 | 25 | 16 | 8 | 32 | **108** |
| 2018 | 21 | 34 | 13 | 4 | 3 | 15 | 5 | 9 | 11 | 17 | 21 | 28 | **181** |
| 2019 | 24 | 9 | 21 | 13 | 14 | 5 | 6 | 13 | 28 | 12 | 13 | 13 | **171** |
| 2020 | 23 | 10 | 16 | 6 | 8 | 14 | 9 | 17 | 21 | 40 | 90 | 123 | **377** |
| 2021 | 60 | 13 | 25 | 30 | 10 | 11 | 10 | 22 | 10 | 31 | 20 | 20 | **262** |
| 2022 | 12 | 6 | 11 | 3 | 7 | 5 | 6 | 2 | 4 | 5 | 8 | 18 | **87** |
| 2023 | 19 | 9 | 16 | 12 | 19 | 24 | 31 | 12 | 38 | 32 | 25 | 38 | **275** |
| 2024 | 15 | 21 | 23 | 20 | 22 | 23 | 22 | 11 | 12 | 14 | 13 | 30 | **226** |
| 2025 | 23 | 25 | 14 | 18 | 41 | 50 | 17 | 19 | 24 | 26 | 14 | 25 | **296** |
| 2026 | 30 | 10 | 14 | 9 | 8 | 10 | 32 | 20 | 10 | . | . | . | **143** |

No gap of two consecutive empty months.

## Tagging hygiene

| group | pins | share |
|---|---|---|
| untagged | 600 | 28.2% |
| exactly one tag | 1094 | 51.5% |
| only workflow tags (no subject) | 0 | 0.0% |
| two or more tags | 432 | 20.3% |

## Tag frequency

| metric | value |
|---|---|
| distinct tags | 502 |
| total tag uses | 2019 |
| share of uses held by the top 40 | 53.2% |
| tags used exactly once | 285 (56.8%) |
| tags used exactly twice | 68 (13.5%) |
| tags used 5 or more times | 85 |

### Head: top 40 tags

| # | tag | pins | share of all pins |
|---|---|---|---|
| 1 | data | 121 | 5.7% |
| 2 | python | 84 | 4.0% |
| 3 | trip | 82 | 3.9% |
| 4 | kids | 71 | 3.3% |
| 5 | book | 69 | 3.2% |
| 6 | ai | 44 | 2.1% |
| 7 | visualization | 42 | 2.0% |
| 8 | physics | 42 | 2.0% |
| 9 | performance | 39 | 1.8% |
| 10 | tool | 36 | 1.7% |
| 11 | job | 34 | 1.6% |
| 12 | pandas | 26 | 1.2% |
| 13 | llm | 24 | 1.1% |
| 14 | ml | 23 | 1.1% |
| 15 | school | 22 | 1.0% |
| 16 | security | 22 | 1.0% |
| 17 | postgres | 20 | 0.9% |
| 18 | music | 18 | 0.8% |
| 19 | climate | 16 | 0.8% |
| 20 | chart | 15 | 0.7% |
| 21 | css | 14 | 0.7% |
| 22 | nature | 14 | 0.7% |
| 23 | testing | 13 | 0.6% |
| 24 | health | 13 | 0.6% |
| 25 | jupyter | 13 | 0.6% |
| 26 | mcp | 11 | 0.5% |
| 27 | stars | 11 | 0.5% |
| 28 | game | 11 | 0.5% |
| 29 | map | 11 | 0.5% |
| 30 | programming | 11 | 0.5% |
| 31 | solar | 11 | 0.5% |
| 32 | opensource | 11 | 0.5% |
| 33 | gdpr | 11 | 0.5% |
| 34 | learning | 10 | 0.5% |
| 35 | duckdb | 10 | 0.5% |
| 36 | presentation | 10 | 0.5% |
| 37 | math | 10 | 0.5% |
| 38 | vibe | 10 | 0.5% |
| 39 | linux | 10 | 0.5% |
| 40 | bike | 10 | 0.5% |

### Long tail

285 tags are used once. First 60 alphabetically: `Ford`, `Lenovo`, `Nvidia`, `OCR`, `OS`, `Productivity`, `SMACK`, `Ubuntu`, `ab`, `aggregations`, `akvarium`, `animals`, `anthropic`, `arrow`, `basecamp`, `basne`, `battleship`, `beach`, `bigdata`, `blender`, `blob`, `brain`, `brainstorm`, `broukbot`, `brucewillis`, `camp`, `cc`, `cdc`, `chat`, `chch`, `chef`, `china`, `chords`, `ci`, `clustering`, `co2`, `coc`, `codegen`, `commerce`, `concussion`, `conservation`, `constellations`, `coop`, `copilot`, `copter`, `corse`, `covid`, `coworking`, `creativity`, `csat`, `curl`, `cycling`, `d3`, `dagster`, `dask`, `databricks`, `datalake`, `dataquality`, `datastory`, `datawarehouse`.

## Near-duplicate tags

No case / separator / plural collisions found.

### Suspected typos

A rare tag one character away from a much more common one.

| suspect | uses | likely meant | uses |
|---|---|---|---|
| `nodes` | 1 | `notes` | 4 |
| `corse` | 1 | `course` | 4 |

## Tag co-occurrence

For each frequent tag, the tags it shares pins with most often (Jaccard similarity).

| tag | travels with (shared pins / jaccard) |
|---|---|
| `data` | `visualization` 10/0.065, `python` 10/0.051, `ai` 5/0.031, `reporting` 3/0.024, `pandas` 3/0.021 |
| `python` | `testing` 6/0.066, `data` 10/0.051, `jupyter` 3/0.032, `ml` 3/0.029, `performance` 3/0.025 |
| `trip` | `nature` 4/0.043, `bird` 3/0.034 |
| `kids` | `school` 6/0.069, `game` 4/0.051, `programming` 4/0.051, `history` 3/0.042, `movies` 3/0.041 |
| `book` | `reading` 3/0.042, `kids` 4/0.029 |
| `ai` | `ml` 3/0.047, `data` 5/0.031 |
| `visualization` | `chart` 7/0.14, `map` 5/0.104, `data` 10/0.065 |
| `physics` | `kids` 4/0.037 |
| `performance` | `javascript` 4/0.095, `postgres` 4/0.073, `python` 3/0.025 |
| `tool` | `image` 3/0.075, `data` 3/0.019 |
| `pandas` | `data` 3/0.021 |
| `llm` | `eval` 3/0.12 |
| `ml` | `ai` 3/0.047, `python` 3/0.029 |
| `school` | `kids` 6/0.069 |
| `postgres` | `performance` 4/0.073 |
| `chart` | `visualization` 7/0.14 |

### Tightest pairs

| pair | shared pins | jaccard |
|---|---|---|
| `electricity` + `game` | 3 | 0.21 |
| `css` + `flex` | 3 | 0.21 |
| `chart` + `visualization` | 7 | 0.14 |
| `eval` + `llm` | 3 | 0.12 |
| `map` + `visualization` | 5 | 0.10 |
| `javascript` + `performance` | 4 | 0.10 |
| `image` + `tool` | 3 | 0.07 |
| `performance` + `postgres` | 4 | 0.07 |
| `kids` + `school` | 6 | 0.07 |
| `python` + `testing` | 6 | 0.07 |
| `data` + `visualization` | 10 | 0.07 |
| `game` + `kids` | 4 | 0.05 |
| `data` + `python` | 10 | 0.05 |
| `kids` + `programming` | 4 | 0.05 |
| `ai` + `ml` | 3 | 0.05 |

## Top domains

| # | domain | pins | share |
|---|---|---|---|
| 1 | github.com | 207 | 9.7% |
| 2 | theguardian.com | 98 | 4.6% |
| 3 | youtube.com | 37 | 1.7% |
| 4 | twitter.com | 35 | 1.6% |
| 5 | medium.com | 22 | 1.0% |
| 6 | bbc.com | 22 | 1.0% |
| 7 | stackoverflow.com | 21 | 1.0% |
| 8 | linkedin.com | 18 | 0.8% |
| 9 | denikn.cz | 18 | 0.8% |
| 10 | link.medium.com | 14 | 0.7% |
| 11 | nytimes.com | 13 | 0.6% |
| 12 | magazin.aktualne.cz | 12 | 0.6% |
| 13 | mobile.twitter.com | 12 | 0.6% |
| 14 | towardsdatascience.com | 11 | 0.5% |
| 15 | dev.to | 11 | 0.5% |
| 16 | edition.cnn.com | 10 | 0.5% |
| 17 | anthropic.com | 9 | 0.4% |
| 18 | startupjobs.cz | 9 | 0.4% |
| 19 | reddit.com | 7 | 0.3% |
| 20 | opensource.com | 7 | 0.3% |
| 21 | blog.google | 6 | 0.3% |
| 22 | zpravy.aktualne.cz | 6 | 0.3% |
| 23 | realpython.com | 6 | 0.3% |
| 24 | wired.com | 6 | 0.3% |
| 25 | elastic.co | 6 | 0.3% |

## `toread` backlog

| metric | value |
|---|---|
| pins marked toread | 39 |
| share of archive | 1.8% |
| median age | 3254 days |
| oldest | 3347 days |
| of those, untagged | 28 |

| age | pins |
|---|---|
| 1-3 years | 1 |
| over 3 years | 38 |

## How the tagging style changed

| year | pins | mean tags / pin | untagged | single tag |
|---|---|---|---|---|
| 2017 | 108 | 0.97 | 30.6% | 46.3% |
| 2018 | 181 | 1.20 | 14.4% | 58.0% |
| 2019 | 171 | 1.09 | 17.0% | 59.1% |
| 2020 | 377 | 1.29 | 6.9% | 62.3% |
| 2021 | 262 | 1.11 | 16.0% | 59.5% |
| 2022 | 87 | 1.18 | 17.2% | 51.7% |
| 2023 | 275 | 0.95 | 22.9% | 61.8% |
| 2024 | 226 | 0.38 | 67.3% | 28.3% |
| 2025 | 296 | 0.87 | 31.4% | 51.0% |
| 2026 | 143 | 0.19 | 84.6% | 11.9% |

## Mechanical merge candidates

Derived by rule, not judgement - every pair here is a spelling of the same idea. Nothing has been renamed; `tags/rename` runs only after you approve.

| fold this | uses | into | uses |
|---|---|---|---|
| `nodes` | 1 | `notes` | 4 |
| `corse` | 1 | `course` | 4 |

<!-- CURATED: hand-written below this line; analyse preserves it -->

# Proposed tag structure

Everything above is computed. Everything below is a proposal, written after
reading a sample of pins behind each ambiguous tag. **Nothing has been renamed.**

## 1. The facets your tags already have

Mapping the top 30 tags onto facets. `topic` is what the thing is *about*,
`type` is what *kind of thing* it is, `status` is what you mean to *do* about it.

| # | tag | uses | facet | note |
|---|---|---|---|---|
| 1 | `data` | 121 | topic | the spine of the archive |
| 2 | `python` | 84 | topic | |
| 3 | `trip` | 73 | topic | |
| 4 | `kids` | 71 | topic | |
| 5 | `book` | 69 | **type** | your only heavily-used type tag |
| 6 | `ai` | 44 | topic | |
| 7 | `physics` | 42 | topic | |
| 8 | `visualization` | 39 | topic | |
| 9 | `performance` | 39 | topic *(aspect)* | a quality, not a subject - see §2 |
| 10 | `job` | 34 | **status** | your only real action tag |
| 11 | `pandas` | 26 | topic | |
| 12 | `llm` | 24 | topic | |
| 13 | `school` | 22 | topic | |
| 14 | `security` | 21 | topic *(aspect)* | |
| 15 | `ml` | 20 | topic | |
| 16 | `tools` | 20 | **type** | split with `tool` |
| 17 | `postgres` | 20 | topic | |
| 18 | `music` | 18 | topic | |
| 19 | `tool` | 16 | **type** | split with `tools` |
| 20 | `css` | 14 | topic | |
| 21 | `nature` | 14 | topic | |
| 22 | `climate` | 14 | topic | |
| 23 | `health` | 13 | topic | |
| 24 | `chart` | 13 | type / topic | ambiguous: the artifact, or the subject |
| 25 | `jupyter` | 13 | topic | |
| 26 | `mcp` | 11 | topic | |
| 27 | `testing` | 11 | topic *(aspect)* | |
| 28 | `stars` | 11 | topic | astronomy |
| 29 | `map` | 11 | type / topic | same ambiguity as `chart` |
| 30 | `programming` | 11 | topic | |

**Tally: 24 topic, 4 type, 1 status, 2 ambiguous.** The vocabulary is a topic
vocabulary with a few type tags mixed in at the same level.

### The facets, sized across the whole archive

| facet | tags in it | uses | share of all tag uses |
|---|---|---|---|
| topic | ~480 | ~1810 | 89% |
| type | `book` 69, `tool`/`tools` 36, `chart` 13, `map` 11, `song` 9, `image` 7, `documentation` 7, `presentation` 7, `game` 7, `midi` 6, `notebook` 5, `movies` 5, `video` 5, `course` 4, `podcast` 2, `slides` 2 | ~195 | 9.6% |
| status | `job` 34, `buy` 5, `inspiration` 5, `gift` 3, `learn` 1, `toread` 1 | 49 | 2.4% |

### An unnamed fourth facet you already use: aspect

`performance` 39, `security` 21, `testing` 11, `privacy` 4, `validation` 3,
`ethics` 2 - about 80 uses. These are cross-cutting qualities, not subjects:
"a Postgres article *about* performance". You apply them consistently, so they
are worth naming as their own facet rather than being filed under topic.

## 2. What is missing or inconsistent

1. **Type is absent from ~90% of pins.** 207 pins are github.com, but `tool` +
   `tools` together are used 36 times. Most repos carry a topic and no type.
2. **The type facet is split three ways.** `tool`/`tools`,
   `presentation`/`slides`, and `notebook` competing with the specific
   `jupyter` (13) and `marimo` (7).
3. **Status is effectively gone.** Pinboard's native `toread` flag carried it
   from 2017 to 2020 and was then abandoned: 26 flagged pins in 2017, 6 in
   2018, 2 in 2019, 4 in 2020, 1 since. The surviving backlog is 39 pins with a
   median age of 8.9 years, 28 of them untagged. That is not a reading list,
   it is a sediment layer.
4. **No language facet, though roughly one pin in seven is Czech**
   (denikn.cz, magazin.aktualne.cz, respekt.cz, plus Czech-titled YouTube).
   Czech content is instead tagged with Czech topic words (`sucho`, `koleda`,
   `vejce`, `kroužky`, `gympl`), which splits topics across two languages.
5. **Case drift**: 6 tags exist in two capitalisations
   (`security`/`Security`, `linux`/`Linux`, `api`/`API`, `cms`/`Cms`,
   `dwh`/`Dwh`, `ansible`/`Ansible`).
6. **Separator drift**: `opensource`/`open-source`, `machine_learning` next to
   `ml`, `note-taking`/`notes`.

**What I am not proposing.** A `status` facet applied going forward would be a
new habit, not a repair - you have never used one, and with 28% of pins
untagged and 51% on a single tag, adding a third required facet would mostly
produce blanks. Reviving the native `toread` flag is the cheaper version of the
same idea. Likewise there is no person facet: `lily` is LilyPond, not a name.

## 3. Canonical vocabulary

**86 tags carry 69% of all tag use** after the merges in §4. Suggested core,
grouped by facet.

**type** (prefer singular): `book`, `tool`, `chart`, `map`, `song`, `image`,
`documentation`, `presentation`, `game`, `midi`, `notebook`, `movies`, `video`,
`course`, `podcast`

**aspect**: `performance`, `security`, `testing`, `privacy`, `validation`

**status**: `job`, `buy`, `inspiration`, `gift`

**topic - data & engineering**: `data`, `python`, `pandas`, `postgres`,
`duckdb`, `sql`, `analytics`, `reporting`, `metadata`, `statistics`, `jupyter`,
`marimo`, `streamlit`, `docker`, `git`, `cli`, `bash`, `linux`, `rust`,
`javascript`, `css`, `ruby`, `elastic`, `drupal`, `android`, `raspberrypi`,
`static`, `opensource`, `graph`, `vault`, `dwh`, `programming`, `remote`,
`management`, `team`, `visualization`, `3d`, `math`

**topic - AI**: `ai`, `llm`, `ml`, `mcp`, `agent`, `vibe`

**topic - science & world**: `physics`, `stars`, `nature`, `climate`, `solar`,
`electricity`, `gdpr`, `health`, `exercise`, `bike`, `car`

**topic - life & family**: `kids`, `school`, `homeschool`, `learning`,
`reading`, `music`, `underground`, `lily`, `trip`, `africa`, `lipno`, `bird`

Below 5 uses is long tail: 446 tags, 300 of them used exactly once. I would
leave the tail alone rather than force it into the core - it is mostly
proper nouns (places, projects, one-off tools) that are doing their job.

## 4. Merge proposals - "fold X into Y"

Applied **locally only**, to `data/pins_clean.json`, by `pins.py clean`. The raw
cache is untouched and Pinboard has not been written to. `pins.py clean --revert`
undoes it. Sending the plan to Pinboard is a separate, deliberate step
(`pins.py rename --yes`).

Result: **532 -> 498 tags, 94 pin edits, 5 duplicate tags collapsed.**
After it, the near-duplicate detector finds nothing left.

### 4a. `case` - local only (8)

`Security`, `Linux`, `API`, `Cms`, `Dwh`, `Ansible`, `Twitter`, `Recommendation`.

**Pinboard already folds these itself.** `tags/get` reports `security: 22`,
which is 21 `security` + 1 `Security` counted as one tag; the same holds for all
six lowercase/uppercase pairs. So for searching and browsing on Pinboard, case
never mattered. It matters only here, because `posts/all` returns the *stored*
per-pin case and local analysis would otherwise count two tags where Pinboard
sees one. `pins.py rename` skips this group automatically - there is nothing on
the Pinboard side to rename.

### 4b. `safe` - plural only (9)

`charts`->`chart`, `games`->`game`, `presentations`->`presentation`,
`birds`->`bird`, `teams`->`team`, `agents`->`agent`, `vectors`->`vector`,
`skills`->`skill`, `tools`->`tool`.

`tools`->`tool` goes against the counts (20 vs 16), to keep the type facet
singular like `book` and `song`.

**Two folds were removed after checking the pins behind them**, and both were
wrong in the same way - a rule-based pass matched a spelling without knowing
the meaning:

| dropped fold | what the pin actually was |
|---|---|
| `corse` -> `course` | Corsica. `rando-patrimoine.corsica`, hiking trails. |
| `nodes` -> `notes` | graph nodes - tagged `graphviz nodes` on a Vega-Lite graph. |

The lesson is now a command: `pins.py show <tag>` prints the pins carrying a
tag, with its time span, so a fold can be checked before it is written down.
No edit-distance fold should enter the plan without it.

### 4c. `separator` (4)

`open-source`->`opensource`, `machine_learning`->`ml`, `js`->`javascript`,
`note-taking`->`notes`.

### 4d. `semantic` - judgement (9)

`travel`->`trip`, `dataviz`->`visualization`, `slides`->`presentation`,
`test`->`testing`, `ops`->`devops`, `container`->`docker`, `pi`->`raspberrypi`,
`assisted`->`vibe`, `agentic`->`agent`.

### 4e. `language` - Czech into English (1)

`klima`->`climate`. That is the whole group; three folds were dropped.

| kept out | why |
|---|---|
| `sucho` (3) | drought is narrower than `climate`; folding loses it |
| `gympl` (2) | not the `school` topic - a two-pin hunt for a specific Prague gymnázium, Dec 2020 |
| `kroužky` (2) | same shape - ornithology clubs at DDM Praha, Aug 2017 |
| `cestykrajem` (3) | a personal NGO plan, kept deliberately |

`gympl` and `kroužky` are what led to section 6.

### 4f. `clarity` - renames, not merges - NOT in the default set

`lily`->`lilypond`, `vault`->`datavault`, `stars`->`astronomy`. Held back;
run with `-g clarity` to include them.

### 4g. Do NOT merge - traps checked against the pins

| tag | uses | looks like | actually is |
|---|---|---|---|
| `graph` | 9 | a chart | graph *databases* and GraphRAG |
| `lily` | 6 | a name | LilyPond, music notation software |
| `vault` | 8 | HashiCorp Vault | Data Vault 2.0 modelling |
| `static` | 9 | a modifier | static site generators |
| `tuber` | 4 | vegetables | Czech YouTubers |
| `underground` | 7 | the tube | Czech underground music |
| `stars` | 11 | GitHub stars | astronomy |
| `svata` | 4 | a place | Svatopluk Karásek, musician |

## 5. Area of life - the second split

Seeding work / family / hunt from existing tags and running it over all 2126:

| | pins | share |
|---|---|---|
| work | 683 | 32% |
| family | 416 | 20% |
| hunt | 64 | 3% |
| tagged, no area signal | 317 | 15% |
| ambiguous (tie) | 46 | 2.2% |
| untagged | 600 | 28% |

**2.2% ambiguous**, and 19 of those 46 ties are caused by tags that are not area
tags at all - `book` (6), `image` (4), `raspberrypi` (2), `music`, `design`,
`video`. Excluding those, true ambiguity is about 1.8%. Area is a learnable
signal.

Two findings that cut against first guesses:

1. **`hunt` is only 3%** of tagged pins, far below intuition. Either the seeds
   are weak, or hunt pins are precisely the ones that never got tagged. The
   backfill will separate these.
2. **The untagged 600 are not a hidden category.** Their domains mirror the
   archive as a whole (github.com 66, theguardian.com 30 - the two top domains
   overall). What they are is *recent*: 33 in 2017 rising to 152 in 2024 and 121
   in 2026. Untagged tracks the collapse of the tagging habit, nothing else.

### Why not prefix topics by group (`ai:llm`, `data:pandas`)

A prefix forces single parenthood, and these tags have two parents - which is
exactly what produced the 19 mis-seeded ties above. `book` is a type, not an
area; `raspberrypi` is work at the office and hobby at home. Grouping is better
kept as a *view* over the tags than as storage: a mapping in this repo can be
wrong and corrected for free, a rename cannot. Topic is also the facet that
already works - 89% of use, unambiguous - so it is the worst place to spend a
migration.

## 6. Bursts: the third category has a shape, not a vocabulary

Seeding `hunt` from tags found only 3% - because a hunt does not reuse your
vocabulary. It invents a throwaway tag, uses it twice in one afternoon, and
never comes back. So look at *timing* instead of words.

Of the 217 tags used more than once, **33 (15%) have every pin inside 60 days**,
most of them inside a single day:

| tag | pins | span | from | what it was |
|---|---|---|---|---|
| `lipno` | 6 | 0d | 2021-10 | booking a cabin |
| `svata` | 4 | 0d | 2020-12 | Svatopluk Karásek |
| `tuber` | 4 | 0d | 2020-12 | Czech YouTubers |
| `koleda` | 4 | 0d | 2020-12 | carol sheet music |
| `sicily` | 3 | 0d | 2024-03 | trip planning |
| `cestykrajem` | 3 | 0d | 2020-12 | the NGO plan |
| `maringotka` | 2 | 0d | 2023-11 | buying a caravan |
| `gympl` | 2 | 0d | 2020-12 | choosing a high school |
| `mia` | 2 | 0d | 2019-05 | water tank and pump |
| `kroužky` | 2 | 0d | 2017-08 | ornithology clubs |

The opposite end is standing interest: `testing` 3261d, `tool` 3091d,
`trip` 3078d, `book` 2968d, `kids` 2908d - tags that span nearly the whole
archive.

### Bursts are two different things

The shape is the same; the intent is not.

- **Hunt** - seeking a *decision*: `lipno`, `maringotka`, `mia`, `gympl`,
  `kroužky`, `sicily`. Practical, one-off, resolved by a purchase or a choice.
- **Binge** - seeking a *subject*: `underground`, `koleda`, `svata`, `gospel`,
  `christmas`, `tuber`, `humanity` - **all of them December 2020**, the single
  busiest month in the archive at 123 pins. One sustained dive into Czech music
  and culture.

Timing separates bursts from standing interests cleanly. Separating a hunt from
a binge needs the content, not the clock.

## 7. `data` is a folder name, not a tag

| | `data` | `trip` |
|---|---|---|
| pins | 121 | 82 |
| span | 2019-2025 | 3078 days, the whole archive |
| sole tag on | **60 pins (50%)** | - |
| top partner | `visualization`, 10 | `nature`, 4 |

On half its pins, `data` is the only tag - so it carries all the information and
distinguishes nothing. At 121 pins it covers roughly **18% of the whole work
domain**. It does not name a topic, it names where you work.

`trip` is the contrast that makes it visible: `trip` maps to an area of life
*and* stays specific inside it. `data` maps to an area and then *is* the area.

### The fix is not new tags

The sub-vocabulary already exists and is being bypassed: `metadata` 9,
`reporting` 9, `analytics` 9, `datavault` 8, `dwh` 4, `modelling` 4,
`validation` 3, `bi` 2. A keyword pass over the 60 sole-`data` pins puts
**24 of them (40%)** onto a tag already in use:

| would take | pins | that tag today |
|---|---|---|
| pipelines | 7 | **0 - does not exist yet** |
| governance | 5 | 1 |
| book | 4 | 69 |
| management | 3 | 8 |
| analytics | 3 | 9 |
| modelling | 2 | 4 |
| no keyword match | 36 | |

Two conclusions, and the second matters for Phase 2:

1. `pipelines` is a genuinely missing tag - 7 pins want it and it does not
   exist. That is a new tag justified by evidence rather than invented.
2. **The other 36 cannot be reached from the title.** "Positron",
   "intake/intake", "Wes McKinney - The Road to Composable Data Systems" are all
   pipeline and tooling pins that no keyword pass can see. Backfilling `data`
   will need the page, not just the title - which sizes the Phase 2 fetch budget
   far above the "only when title is not enough" assumption.
