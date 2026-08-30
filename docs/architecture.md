# Architecture

Three modules, one direction of dependency:

```
cli.py  ->  city.py  ->  economy.py  ->  buildings.py
```

- `buildings.py` — static catalogue of `Building` records. No state.
- `economy.py` — `Economy` holds the treasury and computes tax/upkeep per tick.
- `city.py` — `City` holds the list of placed buildings and owns an `Economy`.
- `cli.py` — argument parsing and printing only.

`_version_generated.py` is written by the release tooling and must never be
hand-edited.


## Derived stats

Two read-only views sit on top of the core state:

- `City.happiness` — a 0-100 score derived from the mix of placed buildings.
  Parks and arcades raise it, factories lower it. It has no effect on the
  economy yet; it exists for the CLI `--report` output.
- `Economy.projected_balance` / `Economy.is_solvent` — a straight-line
  forecast of the treasury given a fixed per-turn delta. Used by planning
  code that wants a cheap "are we heading broke" check without running a
  full simulation.

Both are pure functions of current state and safe to call at any time.
