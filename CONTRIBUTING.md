# Contributing

This is a test fixture, but the rules it enforces are real:

1. **PR title** follows conventional commits: `type(scope): description`
   where `type` is one of `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`.
2. **PR body** links an issue: `Closes #<n>`, `Fixes #<n>`, or `Resolves #<n>`.
3. **PR size** stays under **8 files** and **300 changed lines**
   (additions + deletions), after excluding generated files:
   `uv.lock`, `*.duckdb`, `site/`, `dist/`, `*_generated.*`.

If a change needs more than that, split it into a stack of smaller PRs.

<!-- building data lives in src/tycoon_city/catalogue/ -->
