"""Economic model: treasury, taxes, and upkeep."""

from minicity import buildings

TAX_PER_CITIZEN = 3
TAX_PER_JOB = 2


class Economy:
    def __init__(self, treasury: int = 1000) -> None:
        self.treasury = treasury

    def tax_income(self, population: int, jobs: int) -> int:
        return population * TAX_PER_CITIZEN + jobs * TAX_PER_JOB

    def upkeep_cost(self, placed: list[str]) -> int:
        return sum(buildings.get(name).upkeep for name in placed)

    def tick(self, population: int, jobs: int, placed: list[str]) -> int:
        delta = self.tax_income(population, jobs) - self.upkeep_cost(placed)
        self.treasury += delta
        return delta

    def can_afford(self, name: str) -> bool:
        return self.treasury >= buildings.get(name).cost

    def spend(self, name: str) -> None:
        cost = buildings.get(name).cost
        if cost > self.treasury:
            raise ValueError("insufficient funds")
        self.treasury -= cost

# v0.2.0 release touch
