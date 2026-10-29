# catpin

Analyse a Pinboard archive, then tag fresh pins with help from Claude Code.

**[FINDINGS.md](FINDINGS.md)** is the write-up: what the archive looks like, the
tag decisions and why, and what the next step needs.

## Setup

```sh
uv sync
export PINBOARD_TOKEN='username:HEX'   # pinboard.in/settings/password
```

The token is read from the environment only, and never printed, logged, or put
in an error message.

## Commands

| command | does | writes to Pinboard |
|---|---|---|
| `archive` | fetch `posts/all` + `tags/get` into `data/` | no |
| `clean` | apply `renames.json` to a local copy | no |
| `analyse` | rebuild `data/analysis.md` + `stats.json` | no |
| `show <tag>` | print the pins carrying a tag, with its time span | no |
| `area` | guess each pin's area of life from `areas.json` | no |
| `burst` | tags whose pins all land within a few days | no |
| `rename` | send `renames.json` to Pinboard | **only with `--yes`** |

```sh
uv run pins.py archive
uv run pins.py clean
uv run pins.py analyse
```

`clean` rewrites tags on a **local copy**; the raw cache is never modified and
`clean --revert` drops it. `analyse` prefers `pins_clean.json` when present and
says which source it used. So: try a vocabulary, read the result, edit
`renames.json`, repeat — committing to nothing.

Re-run `analyse` after `clean`: cleaning changes what the analysis can see.
Folding `note-taking` into `notes` is what made the `nodes` typo detectable.

Before adding any fold, check what the tag means:

```sh
uv run pins.py show corse     # -> Corsica, not a typo of "course"
```

### Sending it to Pinboard

```sh
uv run pins.py rename              # dry run
uv run pins.py rename --yes        # apply, ~1 request/second
uv run pins.py rename -g semantic  # one group only
```

Refuses a plan whose result depends on rename order, and re-fetches `tags/get`
afterwards to report which renames actually took effect. The `case` group is
skipped: Pinboard's tag index already folds case (`tags/get` reports
`security: 22` = 21 `security` + 1 `Security`), so there is nothing to rename.

## Rate limits

`posts/all` at most once per five minutes — `archive` enforces this and
`--force` overrides. Everything else ~1 request/second, enforced in the client.

## Files

| path | what | written by | in git |
|---|---|---|---|
| `renames.json` | the merge plan, grouped | you | yes |
| `areas.json` | area-of-life seed tags | you | yes |
| `data/pins_raw.json` | every pin, as Pinboard returned it | `archive` | no |
| `data/pins_clean.json` | the same pins, `renames.json` applied | `clean` | no |
| `data/tags_raw.json` | tag → use count | `archive` | no |
| `data/analysis.md` | the generated report | `analyse` | yes |
| `data/stats.json` | the same numbers, machine-readable | `analyse` | no |
| `data/state.json` | when each endpoint was last called | `archive` | no |

## Reset

```sh
uv run pins.py clean --revert   # drop the local cleanup, keep the cache
rm -rf data/                    # forget everything and re-fetch
```

## Development

```sh
uv run poe check    # lint, typecheck, security, tests
uv run poe fix      # format and autofix
```
