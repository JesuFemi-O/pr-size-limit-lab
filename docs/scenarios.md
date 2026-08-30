# Test scenarios

Each branch opens a PR that exercises one behaviour of the checks.
`main` is the baseline. Every PR uses a conventional-commit title and a
`Closes #<n>` line so that only the size check is under test.

| # | Branch | What it changes | PR Size Check | Why |
| - | ------ | --------------- | ------------- | --- |
| 1 | `feat/small-nightlife-bonus` | 2 files, ~35 lines | ✅ pass | well under both limits |
| 2 | `feat/boundary-8-files` | exactly 8 files, ~290 lines | ✅ pass | sits right on the file limit, just under the line limit |
| 3 | `refactor/split-thirteen-files` | 13 files, ~120 lines | ❌ fail (files) | 13 > 8 even though the line count is small |
| 4 | `feat/big-simulation-rewrite` | 4 files, ~760 lines | ❌ fail (lines) | 4 ≤ 8 files, but 760 > 300 lines — file count alone would miss this |
| 5 | `chore/regenerate-artifacts` | large edits to `uv.lock`, `site/`, `data/*.duckdb`, `*_generated.*` only | ✅ pass | every changed file is on the exclusion list, so counted files = 0 |

Scenario 4 is the one that matters for the proposal's open decision: a
few-file, huge-line PR. `mtfoley/pr-compliance-action` (the doc's "Option A")
has no line or file limit at all, so the custom `pr-size-check.yml` is what
catches 3 and 4.
