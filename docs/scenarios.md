# Test scenarios

`main` ships with `mode: warn` in both `.github/pr-size.yml` and
`.github/pr-title.yml`. Each branch opens a PR that exercises one path.

## PR size check (`scripts/pr_size_check.py`)

| PR branch | Change | Counted files | Check (warn mode) |
| --------- | ------ | ------------- | ----------------- |
| `feat/focused-change` | 4 files, normal edit | 4 / 8 | ✅ green |
| `feat/boundary-eight-files` | exactly 8 counted files | 8 / 8 | ✅ green |
| `feat/too-many-files` | 11 small files | 11 / 8 | ✅ green + ⚠️ warn comment |
| `feat/bundle-weather-template` | new `src/minicity/templates/weather/**` (10 files) + 3 counted | 3 / 8 | ✅ green — template files exempt |
| `feat/oversize-new-module` | new `src/minicity/planner.py` (~479 lines) + 2 edits | 3 / 8 | ✅ green + ⚠️ warn comment (new file > 300 lines) |
| `v0.2.0` → `main` | 16 files (release roll-up) | n/a | ✅ green — release-promotion exemption |
| `chore/require-pr-size` | flips size `mode: warn` → `fail` | 1 / 8 | ✅ green |
| `demo/blocked-under-fail` (base: `chore/require-pr-size`) | 11 files, `mode: fail` | 11 / 8 | ❌ red — blocking |

## PR title check (`scripts/pr_title_check.py`)

| PR branch | Title | Check (warn mode) |
| --------- | ----- | ----------------- |
| `title/ok-gh` | `feat(gh-41): add a small helper` | ✅ green |
| `title/ok-jira` | `fix(PTC-300): stop double-counting renamed files` | ✅ green |
| `title/ok-chore` | `chore(deps): bump the pinned checkout action` | ✅ green |
| `title/missing-ref` | `feat(planner): add a lookahead planner` | ✅ green + ⚠️ warn comment (feat needs `gh-`/`PTC-`) |
| `title/bad-type` | `feature(gh-44): rename the report package` | ✅ green + ⚠️ warn comment (type not allowed) |
| `title/trailing-period` | `docs(gh-45): document the title convention.` | ✅ green + ⚠️ warn comment |
| `title/fix-ci-scope` | `fix(ci): make the size job print totals` | ✅ green + ⚠️ warn comment (`fix` can't use `ci` as scope) |
| `chore/require-pr-title` | flips title `mode: warn` → `fail` | ✅ green |
| `demo/title-blocked-under-fail` (base: `chore/require-pr-title`) | `update stuff` (no type) | ❌ red — blocking |

Each `chore/require-*` branch is the rollout switch; the stacked
`demo/*-blocked-under-fail` branch inherits `mode: fail` from its base and
shows what enforcement looks like, while every PR against `main` stays
non-blocking until the flip merges.
