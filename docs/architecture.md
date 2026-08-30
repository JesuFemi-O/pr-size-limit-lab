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

<!-- reviewed for v0.2.0 -->
