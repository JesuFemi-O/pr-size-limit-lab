"""City state: the grid of placed buildings and derived stats."""

from minicity import buildings
from minicity.economy import Economy


class City:
    def __init__(self, name: str = "Toyville", treasury: int = 1000) -> None:
        self.name = name
        self.placed: list[str] = []
        self.economy = Economy(treasury)
        self.turn = 0

    @property
    def population(self) -> int:
        return sum(buildings.get(n).population for n in self.placed)

    @property
    def jobs(self) -> int:
        return sum(buildings.get(n).jobs for n in self.placed)

    def build(self, name: str) -> None:
        building = buildings.get(name)
        self.economy.spend(name)
        self.placed.append(building.name)

    def advance(self) -> int:
        self.turn += 1
        return self.economy.tick(self.population, self.jobs, self.placed)

    def summary(self) -> dict[str, int | str]:
        return {
            "name": self.name,
            "turn": self.turn,
            "population": self.population,
            "jobs": self.jobs,
            "treasury": self.economy.treasury,
            "buildings": len(self.placed),
        }
