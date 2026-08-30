# tycoon-city-lab

A deliberately tiny toy CLI used as a **fixture repo** for testing the
contributor-UX PR-size-limit proposal.

It is not a real product. The code models a toy city so that pull requests
have something plausible to change.

## What lives here

| Path | Purpose |
| --- | --- |
| `src/tycoon_city/` | toy CLI + city simulation |
| `tests/` | pytest suite |
| `site/` | "generated" static docs site (excluded from PR size counts) |
| `data/*.duckdb` | "generated" data artifacts (excluded from PR size counts) |
| `src/tycoon_city/_version_generated.py` | "generated" version stamp (excluded) |
| `.github/workflows/pr-compliance.yml` | conventional-commit title + linked-issue check |
| `.github/workflows/pr-size-check.yml` | files ≤ 8 and lines ≤ 300 check |

## Enforcement under test

- **Title**: conventional commits (`type(scope): description`)
- **Linked issue**: PR body must contain `Closes #<n>` / `Fixes #<n>` / `Resolves #<n>`
- **Size**: max 8 files changed, max 300 lines (additions + deletions) changed,
  after excluding `uv.lock`, `*.duckdb`, `site/`, `dist/`, `*_generated.*`

See `docs/scenarios.md` for the branches that exercise each rule.
