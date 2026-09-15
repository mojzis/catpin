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
| distinct tags | 532 |
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
| exactly one tag | 1091 | 51.3% |
| only workflow tags (no subject) | 0 | 0.0% |
| two or more tags | 435 | 20.5% |

## Tag frequency

| metric | value |
|---|---|
| distinct tags | 532 |
| total tag uses | 2024 |
| share of uses held by the top 40 | 51.2% |
| tags used exactly once | 300 (56.4%) |
| tags used exactly twice | 78 (14.7%) |
| tags used 5 or more times | 85 |

### Head: top 40 tags

| # | tag | pins | share of all pins |
|---|---|---|---|
| 1 | data | 121 | 5.7% |
| 2 | python | 84 | 4.0% |
| 3 | trip | 73 | 3.4% |
| 4 | kids | 71 | 3.3% |
| 5 | book | 69 | 3.2% |
| 6 | ai | 44 | 2.1% |
| 7 | physics | 42 | 2.0% |
| 8 | visualization | 39 | 1.8% |
| 9 | performance | 39 | 1.8% |
| 10 | job | 34 | 1.6% |
| 11 | pandas | 26 | 1.2% |
| 12 | llm | 24 | 1.1% |
| 13 | school | 22 | 1.0% |
| 14 | security | 21 | 1.0% |
| 15 | ml | 20 | 0.9% |
| 16 | tools | 20 | 0.9% |
| 17 | postgres | 20 | 0.9% |
| 18 | music | 18 | 0.8% |
| 19 | tool | 16 | 0.8% |
| 20 | css | 14 | 0.7% |
| 21 | nature | 14 | 0.7% |
| 22 | climate | 14 | 0.7% |
| 23 | health | 13 | 0.6% |
| 24 | chart | 13 | 0.6% |
| 25 | jupyter | 13 | 0.6% |
| 26 | mcp | 11 | 0.5% |
| 27 | testing | 11 | 0.5% |
| 28 | stars | 11 | 0.5% |
| 29 | map | 11 | 0.5% |
| 30 | programming | 11 | 0.5% |
| 31 | solar | 11 | 0.5% |
| 32 | gdpr | 11 | 0.5% |
| 33 | learning | 10 | 0.5% |
| 34 | duckdb | 10 | 0.5% |
| 35 | math | 10 | 0.5% |
| 36 | bike | 10 | 0.5% |
| 37 | graph | 9 | 0.4% |
| 38 | metadata | 9 | 0.4% |
| 39 | linux | 9 | 0.4% |
| 40 | song | 9 | 0.4% |

### Long tail

300 tags are used once. First 60 alphabetically: `API`, `Ansible`, `Cms`, `Dwh`, `Ford`, `Lenovo`, `Linux`, `Nvidia`, `OCR`, `OS`, `Productivity`, `Recommendation`, `SMACK`, `Security`, `Ubuntu`, `ab`, `agents`, `aggregations`, `akvarium`, `animals`, `ansible`, `anthropic`, `api`, `arrow`, `basecamp`, `basne`, `battleship`, `beach`, `bigdata`, `blender`, `blob`, `brain`, `brainstorm`, `broukbot`, `brucewillis`, `camp`, `cc`, `cdc`, `chat`, `chch`, `chef`, `china`, `chords`, `ci`, `clustering`, `co2`, `coc`, `codegen`, `commerce`, `concussion`, `conservation`, `constellations`, `coop`, `copilot`, `copter`, `corse`, `covid`, `coworking`, `creativity`, `csat`.

## Near-duplicate tags

Tags that collapse to the same key once case, separators and plurals are folded.

| kind | variants (uses) | combined |
|---|---|---|
| plural | `tools` (20), `tool` (16) | 36 |
| case | `security` (21), `Security` (1) | 22 |
| plural | `chart` (13), `charts` (2) | 15 |
| plural | `game` (7), `games` (4) | 11 |
| case | `linux` (9), `Linux` (1) | 10 |
| plural | `presentation` (7), `presentations` (2) | 9 |
| plural | `bird` (6), `birds` (2) | 8 |
| plural | `team` (6), `teams` (1) | 7 |
| case | `dwh` (3), `Dwh` (1) | 4 |
| case | `cms` (3), `Cms` (1) | 4 |
| plural | `agent` (2), `agents` (1) | 3 |
| plural | `vector` (2), `vectors` (1) | 3 |
| plural | `skill` (1), `skills` (1) | 2 |
| case | `api` (1), `API` (1) | 2 |
| plural | `recommendations` (1), `Recommendation` (1) | 2 |
| case | `ansible` (1), `Ansible` (1) | 2 |

### Suspected typos

A rare tag one character away from a much more common one.

| suspect | uses | likely meant | uses |
|---|---|---|---|
| `corse` | 1 | `course` | 4 |

## Tag co-occurrence

For each frequent tag, the tags it shares pins with most often (Jaccard similarity).

| tag | travels with (shared pins / jaccard) |
|---|---|
| `data` | `visualization` 9/0.06, `python` 10/0.051, `ai` 5/0.031, `reporting` 3/0.024, `tools` 3/0.022 |
| `python` | `testing` 6/0.067, `data` 10/0.051, `jupyter` 3/0.032, `ml` 3/0.03, `performance` 3/0.025 |
| `trip` | `nature` 4/0.048 |
| `kids` | `school` 6/0.069, `programming` 4/0.051, `history` 3/0.042, `games` 3/0.042, `movies` 3/0.041 |
| `book` | `reading` 3/0.042, `kids` 4/0.029 |
| `ai` | `data` 5/0.031 |
| `physics` | `kids` 4/0.037 |
| `visualization` | `chart` 6/0.13, `map` 5/0.111, `data` 9/0.06 |
| `performance` | `javascript` 3/0.075, `postgres` 4/0.073, `python` 3/0.025 |
| `pandas` | `data` 3/0.021 |
| `llm` | `eval` 3/0.12 |
| `school` | `kids` 6/0.069 |
| `ml` | `python` 3/0.03 |
| `tools` | `data` 3/0.022 |
| `postgres` | `performance` 4/0.073 |
| `css` | `flex` 3/0.214 |

### Tightest pairs

| pair | shared pins | jaccard |
|---|---|---|
| `electricity` + `game` | 3 | 0.30 |
| `css` + `flex` | 3 | 0.21 |
| `chart` + `visualization` | 6 | 0.13 |
| `eval` + `llm` | 3 | 0.12 |
| `map` + `visualization` | 5 | 0.11 |
| `javascript` + `performance` | 3 | 0.07 |
| `performance` + `postgres` | 4 | 0.07 |
| `kids` + `school` | 6 | 0.07 |
| `python` + `testing` | 6 | 0.07 |
| `data` + `visualization` | 9 | 0.06 |
| `data` + `python` | 10 | 0.05 |
| `kids` + `programming` | 4 | 0.05 |
| `nature` + `trip` | 4 | 0.05 |
| `book` + `reading` | 3 | 0.04 |
| `history` + `kids` | 3 | 0.04 |

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
| 2017 | 108 | 0.98 | 30.6% | 45.4% |
| 2018 | 181 | 1.20 | 14.4% | 58.0% |
| 2019 | 171 | 1.09 | 17.0% | 59.1% |
| 2020 | 377 | 1.29 | 6.9% | 61.8% |
| 2021 | 262 | 1.12 | 16.0% | 59.5% |
| 2022 | 87 | 1.20 | 17.2% | 51.7% |
| 2023 | 275 | 0.95 | 22.9% | 61.8% |
| 2024 | 226 | 0.38 | 67.3% | 28.3% |
| 2025 | 296 | 0.87 | 31.4% | 51.0% |
| 2026 | 143 | 0.19 | 84.6% | 11.9% |

## Mechanical merge candidates

Derived by rule, not judgement - every pair here is a spelling of the same idea. Nothing has been renamed; `tags/rename` runs only after you approve.

| fold this | uses | into | uses |
|---|---|---|---|
| `tool` | 16 | `tools` | 20 |
| `Security` | 1 | `security` | 21 |
| `charts` | 2 | `chart` | 13 |
| `games` | 4 | `game` | 7 |
| `Linux` | 1 | `linux` | 9 |
| `presentations` | 2 | `presentation` | 7 |
| `birds` | 2 | `bird` | 6 |
| `teams` | 1 | `team` | 6 |
| `Dwh` | 1 | `dwh` | 3 |
| `Cms` | 1 | `cms` | 3 |
| `agents` | 1 | `agent` | 2 |
| `vectors` | 1 | `vector` | 2 |
| `skills` | 1 | `skill` | 1 |
| `API` | 1 | `api` | 1 |
| `Recommendation` | 1 | `recommendations` | 1 |
| `Ansible` | 1 | `ansible` | 1 |
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

Nothing below has been applied. Renames go through `tags/rename`, one call
each, after you say which lines to take.

### 4a. Safe: case, plural and one typo (18)

| fold | uses | into | uses | result |
|---|---|---|---|---|
| `Security` | 1 | `security` | 21 | 22 |
| `Linux` | 1 | `linux` | 9 | 10 |
| `Dwh` | 1 | `dwh` | 3 | 4 |
| `Cms` | 1 | `cms` | 3 | 4 |
| `API` | 1 | `api` | 1 | 2 |
| `Ansible` | 1 | `ansible` | 1 | 2 |
| `Twitter` | 2 | `twitter` | 0 | 2 |
| `charts` | 2 | `chart` | 13 | 15 |
| `games` | 4 | `game` | 7 | 11 |
| `presentations` | 2 | `presentation` | 7 | 9 |
| `birds` | 2 | `bird` | 6 | 8 |
| `teams` | 1 | `team` | 6 | 7 |
| `agents` | 1 | `agent` | 2 | 3 |
| `vectors` | 1 | `vector` | 2 | 3 |
| `skills` | 1 | `skill` | 1 | 2 |
| `Recommendation` | 1 | `recommendations` | 1 | 2 |
| `corse` | 1 | `course` | 4 | 5 |
| `tools` | 20 | `tool` | 16 | 36 |

The last line goes *against* the counts, to keep the type facet singular like
`book` and `song`. Say the word and I will flip it to `tools`.

### 4b. Separator and spelling the rule-based pass missed (4)

| fold | uses | into | uses | result |
|---|---|---|---|---|
| `open-source` | 3 | `opensource` | 8 | 11 |
| `machine_learning` | 3 | `ml` | 20 | 23 |
| `js` | 3 | `javascript` | 4 | 7 |
| `note-taking` | 2 | `notes` | 2 | 4 |

### 4c. Same idea, different word - my judgement, your call (9)

| fold | uses | into | uses | result | why |
|---|---|---|---|---|---|
| `travel` | 9 | `trip` | 73 | 82 | same pins in kind |
| `dataviz` | 5 | `visualization` | 39 | 44 | |
| `slides` | 2 | `presentation` | 7 | 9 | |
| `test` | 2 | `testing` | 11 | 13 | |
| `ops` | 2 | `devops` | 2 | 4 | |
| `container` | 2 | `docker` | 8 | 10 | every pin is Docker |
| `pi` | 3 | `raspberrypi` | 4 | 7 | |
| `assisted` | 4 | `vibe` | 6 | 10 | both are AI-assisted coding |
| `agentic` | 2 | `agent` | 2 | 4 | |

### 4d. Czech into English (3 sure, 2 to decide)

| fold | uses | into | uses | confidence |
|---|---|---|---|---|
| `klima` | 2 | `climate` | 14 | sure |
| `gympl` | 2 | `school` | 22 | sure |
| `cestykrajem` | 3 | `trip` | 73 | sure |
| `sucho` | 3 | `climate` | 14 | **decide** - drought is narrower than climate |
| `kroužky` | 2 | `kids` or `school` | | **decide** - which one? |

### 4e. Do NOT merge - traps I checked

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

### 4f. Renames for clarity, not merges - optional (3)

`lily` -> `lilypond`, `vault` -> `datavault`, `stars` -> `astronomy`.
Each is one `tags/rename` call and makes the trap above go away permanently.

## 5. What I need from you

1. Take 4a and 4b wholesale? (22 renames, all mechanical)
2. Which lines of 4c do you want?
3. `sucho` and `kroužky` in 4d - fold where?
4. `tool` or `tools` as the canonical type tag?
5. The optional renames in 4f - yes or no?
6. For Phase 2: should the tagging tool ever propose a **type** tag and an
   **aspect** tag, or stick to topic only? Type is your weakest facet, so
   proposing one per pin is the highest-value habit change available - but it
   is a change, so it is yours to choose.
