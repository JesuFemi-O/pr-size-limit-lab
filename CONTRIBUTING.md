# Contributing

This is a sandbox, but the rules it enforces are real proposals.

## PR title — [`docs/proposal-title.md`](docs/proposal-title.md)

Format: `type(scope): description`

- `type` is one of `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`.
- For `feat`, `fix`, `refactor`, `test`, `docs` the scope is an issue /
  ticket reference: `gh-<N>` (a GitHub issue here) or `PTC-<N>` (a Jira
  ticket). Example: `feat(gh-128): add layer materialization command`.
- For `chore` and `ci` the scope is free-form but must be present:
  `chore(deps): bump typer to 0.16`.
- The description must not end with a period. The whole title must be ≤ 100
  characters.

## PR size — [`docs/proposal.md`](docs/proposal.md)

1. **A PR changes at most 8 counted files.** Added, modified, deleted, and
   renamed files all count.
2. Files under `src/minicity/templates/**` do **not** count — a template
   bundle is atomic and splitting it would leave broken intermediate states.
3. A PR from a `vX.Y.Z` branch into `main` is fully exempt.
4. A newly **added** `src/**/*.py` file may not exceed 300 lines. Modifying
   an already-large module is fine.

If a change needs more than 8 files, submit it as a stack of smaller PRs —
pick the right base branch manually, or use
[`gh-stack`](https://github.github.com/gh-stack/).

Both checks run in `warn` mode during rollout (`mode:` in
`.github/pr-size.yml` / `.github/pr-title.yml`): violations are reported but
do not block.
