# Test scenarios

`main` ships with `mode: warn` in `.github/pr-size.yml`. Each branch opens a
PR that exercises one path through `scripts/pr_size_check.py`.

| PR branch | Change | Counted files | Check (warn mode) |
| --------- | ------ | ------------- | ----------------- |
| `feat/focused-change` | 4 files, normal edit | 4 / 8 | ✅ green |
| `feat/boundary-eight-files` | exactly 8 counted files | 8 / 8 | ✅ green |
| `feat/too-many-files` | 11 small files | 11 / 8 | ✅ green + ⚠️ warn comment |
| `feat/bundle-weather-template` | new `src/minicity/templates/weather/**` (10 files) + 3 counted | 3 / 8 | ✅ green — template files exempt |
| `feat/oversize-new-module` | new `src/minicity/planner.py` (~479 lines) + 2 edits | 3 / 8 | ✅ green + ⚠️ warn comment (new file > 300 lines) |
| `v0.2.0` → `main` | 16 files (release roll-up) | n/a | ✅ green — release-promotion exemption |
| `chore/require-pr-size` | flips `mode: warn` → `fail` | 1 / 8 | ✅ green |
| `demo/blocked-under-fail` (base: `chore/require-pr-size`) | 11 files, runs with `mode: fail` | 11 / 8 | ❌ red — blocking |

The last two show the switch: `demo/blocked-under-fail` is stacked on
`chore/require-pr-size`, so its check reads `mode: fail` and blocks, while
every PR against `main` stays non-blocking until the flip merges.

<!-- reviewed for v0.2.0 -->
