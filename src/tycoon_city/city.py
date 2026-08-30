"""City state: the grid of placed buildings and derived stats."""

from tycoon_city import buildings
from tycoon_city.economy import Economy


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


    @property
    def happiness(self) -> int:
        """Rough happiness score: parks help, factories hurt."""
        score = 50
        score += 5 * self.placed.count("park")
        score += 3 * self.placed.count("arcade")
        score -= 4 * self.placed.count("factory")
        return max(0, min(100, score))

    def report(self) -> list[str]:
        lines = [f"{self.name} — turn {self.turn}"]
        for key, value in self.summary().items():
            lines.append(f"  {key}: {value}")
        lines.append(f"  happiness: {self.happiness}")
        return lines
