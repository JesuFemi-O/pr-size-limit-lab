"""Economic model: treasury, taxes, and upkeep."""

from tycoon_city import buildings

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


    def projected_balance(self, per_turn_delta: int, turns: int) -> int:
        """Treasury after `turns` more turns at a fixed per-turn delta."""
        return self.treasury + per_turn_delta * turns

    def is_solvent(self, per_turn_delta: int, turns: int = 5) -> bool:
        return self.projected_balance(per_turn_delta, turns) >= 0
