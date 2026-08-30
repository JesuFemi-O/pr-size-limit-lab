from dataclasses import dataclass


@dataclass(frozen=True)
class Building:
    name: str
    cost: int
    upkeep: int
    jobs: int
    population: int
