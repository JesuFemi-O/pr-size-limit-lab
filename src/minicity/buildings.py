"""Building catalogue for the toy city."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Building:
    name: str
    cost: int
    upkeep: int
    jobs: int
    population: int


CATALOGUE: dict[str, Building] = {
    "house": Building("house", cost=100, upkeep=2, jobs=0, population=4),
    "shop": Building("shop", cost=250, upkeep=5, jobs=6, population=0),
    "factory": Building("factory", cost=600, upkeep=12, jobs=20, population=0),
    "park": Building("park", cost=150, upkeep=3, jobs=1, population=0),
    "arcade": Building("arcade", cost=400, upkeep=8, jobs=10, population=0),
}


def get(name: str) -> Building:
    try:
        return CATALOGUE[name]
    except KeyError:
        raise ValueError(f"unknown building: {name!r}") from None


def names() -> list[str]:
    return sorted(CATALOGUE)

def costliest() -> str:
    return max(CATALOGUE, key=lambda n: CATALOGUE[n].cost)
