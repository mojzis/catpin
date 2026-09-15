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
| oldest | 3348 days |
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

Interpretation, decisions and open questions live in `../FINDINGS.md`.
This file is generated; anything written below this marker survives `analyse`.
