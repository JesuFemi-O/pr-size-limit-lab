# pr-size-limit-lab

An isolated sandbox for validating **PR CI checks** as code before they go
anywhere real.

The application code (a toy `minicity` CLI under `src/minicity/`) exists only
so that pull requests have something plausible to change.

Two checks, each a small dependency-free script + its own workflow + its own
config file, each with a `warn` → `fail` switch:

| Check | Script | Workflow | Config | Spec |
| --- | --- | --- | --- | --- |
| PR size | `scripts/pr_size_check.py` | `.github/workflows/pr-size.yml` | `.github/pr-size.yml` | [`docs/proposal.md`](docs/proposal.md) |
| PR title | `scripts/pr_title_check.py` | `.github/workflows/pr-title.yml` | `.github/pr-title.yml` | [`docs/proposal-title.md`](docs/proposal-title.md) |

## PR size

| Rule | Value | Notes |
| --- | --- | --- |
| Counted files changed | ≤ **8** | union of added/modified/deleted/renamed paths |
| Exempt from the count | `src/minicity/templates/**` | template bundles are atomic |
| Fully exempt PRs | head branch `^v\d+\.\d+\.\d+$` → `main` | release-promotion roll-ups |
| New-file line cap | **300** lines | only files *added* under `src/**/*.py` |

## PR title

Format `type(scope): description`.

| type | scope | example |
| --- | --- | --- |
| `feat` `fix` `refactor` `test` `docs` | `gh-<N>` or `PTC-<N>` | `feat(gh-128): add layer materialization command` |
| `chore` `ci` | free-form, non-empty | `chore(deps): bump typer to 0.16` |

Description present, no trailing period; whole title ≤ **100** chars.
Release-promotion branches and `ignore_authors` are exempt.

## warn vs fail

`mode:` in each check's config file is the single switch:

- `warn` — violations are reported (job summary, a sticky PR comment, and
  `::warning::` annotations) but the check stays green. This is the rollout
  phase.
- `fail` — a violation fails the check and blocks the merge.

Flipping that one line (or setting the `PR_SIZE_MODE` / `PR_TITLE_MODE` repo
variable) is the entire "make it required" step.
[`docs/scenarios.md`](docs/scenarios.md) lists the PRs that exercise each
path.
