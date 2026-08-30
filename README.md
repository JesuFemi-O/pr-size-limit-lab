# pr-size-limit-lab

An isolated sandbox for validating a **PR size limit** as a CI check before
it goes anywhere real.

The application code (a toy `minicity` CLI under `src/minicity/`) exists only so
that pull requests have something plausible to change.

The rule under test is written up in [`docs/proposal.md`](docs/proposal.md).

## The check

`.github/workflows/pr-size.yml` + `scripts/pr_size_check.py`, configured by
`.github/pr-size.yml`:

| Rule | Value | Notes |
| --- | --- | --- |
| Counted files changed | ≤ **8** | union of added/modified/deleted/renamed paths |
| Exempt from the count | `src/minicity/templates/**` | template bundles are atomic |
| Fully exempt PRs | head branch `^v\d+\.\d+\.\d+$` → `main` | release-promotion roll-ups |
| New-file line cap | **300** lines | only files *added* under `src/**/*.py` |

### warn vs fail

`mode:` in `.github/pr-size.yml` is the single switch:

- `warn` — violations are reported (job summary, a sticky PR comment, and
  `::warning::` annotations) but the check stays green. This is the rollout
  phase.
- `fail` — a violation fails the check and blocks the merge.

Flipping that one line (or setting the `PR_SIZE_MODE` repo variable) is the
entire "make it required" step. [`docs/scenarios.md`](docs/scenarios.md)
lists the PRs that exercise each path.

<!-- v0.2.0 -->
