# Test scenarios

`main` ships with `mode: warn` in `.github/pr-size.yml`. Each branch opens a
PR that exercises one path through `scripts/pr_size_check.py`.

| # | Branch | Change | Counted files | Check (warn mode) |
| - | ------ | ------ | ------------- | ----------------- |
| 1 | `feat/focused-change` | 4 files, normal edit | 4 / 8 | ✅ green, no comment |
| 2 | `feat/boundary-eight-files` | exactly 8 counted files | 8 / 8 | ✅ green |
| 3 | `feat/too-many-files` | 11 files, small edits | 11 / 8 | ✅ green + ⚠️ warn comment |
| 4 | `feat/bundle-weather-template` | new `src/tycoon/templates/weather/**` (10 files) + 3 real files | 3 / 8 | ✅ green — template files exempt |
| 5 | `feat/oversize-new-module` | new `src/tycoon/planner.py` (~430 lines) + 2 edits | 3 / 8 | ✅ green + ⚠️ warn comment (new-file > 300) |
| 6 | `v0.2.0` → `main` | 15 files (release roll-up) | n/a | ✅ green — release-promotion exemption |
| 7 | `chore/require-pr-size` | flips `mode: warn` → `fail` | 1 / 8 | ✅ green |
| 8 | `demo/blocked-under-fail` (base: `chore/require-pr-size`) | 11 files, runs with `mode: fail` | 11 / 8 | ❌ red — blocking |

Scenarios 7 + 8 show the switch: 8 is stacked on 7, so its check reads
`mode: fail` and blocks, while every PR against `main` stays non-blocking
until 7 merges.

<!-- reviewed for v0.2.0 -->
