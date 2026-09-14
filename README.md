# catpin

Analyse a Pinboard archive, then tag fresh pins with help from Claude Code.

## Setup

```sh
uv sync
export PINBOARD_TOKEN='username:HEX'   # from https://pinboard.in/settings/password
```

The token is read from the environment only. It is never printed, logged, or
included in an error message.

## Phase 1 — analysis

```sh
uv run pins.py archive    # posts/all + tags/get -> data/pins_raw.json, data/tags_raw.json
uv run pins.py analyse    # -> data/analysis.md, data/stats.json
```

`archive` refuses to call `posts/all` more than once every five minutes, which is
Pinboard's published limit; `--force` overrides it. `analyse` never touches the
network, so it is free to re-run.

Anything written below the `<!-- CURATED -->` marker at the bottom of
`data/analysis.md` is hand-maintained and survives a re-run of `analyse`.

## Where state lives

| path | what it is | written by |
|---|---|---|
| `data/pins_raw.json` | every pin, exactly as Pinboard returned it | `archive` |
| `data/tags_raw.json` | tag -> use count | `archive` |
| `data/analysis.md` | the readable report | `analyse` |
| `data/stats.json` | the same numbers, machine-readable | `analyse` |
| `data/state.json` | when each endpoint was last called | `archive` |

Everything under `data/` is gitignored: it is your data, not the tool's.

## Reset

```sh
rm -rf data/            # forget the cache and start over
rm data/state.json      # forget the rate-limit cooldown only
```

## Development

```sh
uv run poe check        # lint, typecheck, security, tests
uv run poe fix          # format and autofix
```
