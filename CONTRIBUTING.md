# Contributing

This is a sandbox, but the size rule it enforces is the one described in
[`docs/proposal.md`](docs/proposal.md):

1. **A PR changes at most 8 counted files.** Added, modified, deleted, and
   renamed files all count.
2. Files under `src/tycoon/templates/**` do **not** count — a template bundle
   is atomic and splitting it would leave broken intermediate states.
3. A PR from a `vX.Y.Z` branch into `main` is fully exempt — it rolls up
   changes already reviewed during the release cycle.
4. A newly **added** `src/**/*.py` file may not exceed 300 lines. Modifying an
   already-large module is fine.

If a change needs more than 8 files, submit it as a stack of smaller PRs —
pick the right base branch manually, or use
[`gh-stack`](https://github.github.com/gh-stack/).

During the rollout phase (`mode: warn` in `.github/pr-size.yml`) violations
are reported but do not block.
