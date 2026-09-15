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
uv run pins.py clean      # apply renames.json to a local copy -> data/pins_clean.json
uv run pins.py analyse    # -> data/analysis.md, data/stats.json
```

`clean` rewrites tags on a **local copy only**. Pinboard is never contacted, the
raw cache is never modified, and `clean --revert` deletes the copy. `analyse`
prefers `pins_clean.json` when it exists and says which source it used, so you
can try a vocabulary, read the result, adjust `renames.json`, and repeat without
committing to anything.

Cleaning changes what the analysis can see, so it is worth re-running: folding
`note-taking` into `notes` is what made the `nodes` typo detectable.

### Sending the cleanup to Pinboard

```sh
uv run pins.py rename              # dry run, one line per rename
uv run pins.py rename --yes        # actually apply, ~1 request/second
uv run pins.py rename -g semantic  # just one group
```

This is the only command in Phase 1 that writes to Pinboard, and it needs
`--yes`. It refuses a plan whose result would depend on the order renames run
in, and afterwards re-fetches `tags/get` to report which ones actually took
effect.

The `case` group is skipped automatically: Pinboard's tag index already folds
case (`tags/get` reports `security: 22` = 21 `security` + 1 `Security`), so
there is nothing to rename there. It is applied locally only, because
`posts/all` returns the stored per-pin case.

`archive` refuses to call `posts/all` more than once every five minutes, which is
Pinboard's published limit; `--force` overrides it. `analyse` never touches the
network, so it is free to re-run.

Anything written below the `<!-- CURATED -->` marker at the bottom of
`data/analysis.md` is hand-maintained and survives a re-run of `analyse`.

## Where state lives

| path | what it is | written by |
|---|---|---|
| `data/pins_raw.json` | every pin, exactly as Pinboard returned it | `archive` |
| `data/pins_clean.json` | the same pins with `renames.json` applied | `clean` |
| `renames.json` | the merge plan, grouped; tracked in git | you |
| `data/tags_raw.json` | tag -> use count | `archive` |
| `data/analysis.md` | the readable report | `analyse` |
| `data/stats.json` | the same numbers, machine-readable | `analyse` |
| `data/state.json` | when each endpoint was last called | `archive` |

Everything under `data/` is gitignored: it is your data, not the tool's.

## Reset

```sh
uv run pins.py clean --revert   # drop the local cleanup, keep the cache
rm -rf data/                    # forget everything and re-fetch
rm data/state.json              # forget the rate-limit cooldown only
```

## Development

```sh
uv run poe check        # lint, typecheck, security, tests
uv run poe fix          # format and autofix
```
