"""Multi-turn planner: depth-first search over build orders."""

from __future__ import annotations

from dataclasses import dataclass, field

from tycoon_city import buildings
from tycoon_city.city import City

MAX_LOOKAHEAD = 6


def happiness_of(placed: list[str]) -> int:
    """Local happiness estimate so the planner does not depend on City internals."""
    score = 50
    score += 5 * placed.count("park")
    score += 3 * placed.count("arcade")
    score -= 4 * placed.count("factory")
    return max(0, min(100, score))


@dataclass
class PlanStep:
    turn: int
    action: str
    building: str | None
    treasury_after: int
    happiness_after: int
    population_after: int


@dataclass
class Plan:
    steps: list[PlanStep] = field(default_factory=list)
    score: float = 0.0

    @property
    def build_order(self) -> list[str]:
        return [s.building for s in self.steps if s.building is not None]

    @property
    def turns(self) -> int:
        return len(self.steps)

    def describe(self) -> list[str]:
        out = [f"plan score={self.score:.1f} over {self.turns} turns"]
        for step in self.steps:
            tag = step.building or "wait"
            out.append(
                f"  t{step.turn}: {tag:<8} "
                f"treasury={step.treasury_after} "
                f"pop={step.population_after} "
                f"happiness={step.happiness_after}"
            )
        return out


class Planner:
    def __init__(self, goal: str = "balanced", lookahead: int = 4) -> None:
        if lookahead > MAX_LOOKAHEAD:
            raise ValueError(f"lookahead {lookahead} exceeds {MAX_LOOKAHEAD}")
        if lookahead < 1:
            raise ValueError("lookahead must be at least 1")
        self.goal = goal
        self.lookahead = lookahead
        self._nodes_visited = 0

    @property
    def nodes_visited(self) -> int:
        return self._nodes_visited

    def _score(self, city: City) -> float:
        summary = city.summary()
        treasury = int(summary["treasury"])
        population = int(summary["population"])
        jobs = int(summary["jobs"])
        happiness = happiness_of(city.placed)
        if self.goal == "growth":
            return population * 10 + treasury * 0.1
        if self.goal == "profit":
            return treasury * 1.0
        if self.goal == "happy":
            return happiness * 5.0 + population * 2
        if self.goal == "jobs":
            return jobs * 8.0 + population * 2
        return population * 4 + happiness * 2 + jobs * 1.5 + treasury * 0.05

    def _candidates(self, city: City) -> list[str | None]:
        options: list[str | None] = [None]
        for name in buildings.names():
            if city.economy.can_afford(name):
                options.append(name)
        return options

    def plan(self, city: City) -> Plan:
        self._nodes_visited = 0
        best = Plan(score=float("-inf"))
        self._search(city, depth=0, steps=[], best=best)
        if best.score == float("-inf"):
            return Plan()
        return best

    def _search(
        self,
        city: City,
        depth: int,
        steps: list[PlanStep],
        best: Plan,
    ) -> None:
        self._nodes_visited += 1
        if depth == self.lookahead:
            score = self._score(city)
            if score > best.score:
                best.score = score
                best.steps = list(steps)
            return

        for choice in self._candidates(city):
            branch = _clone(city)
            if choice is not None:
                try:
                    branch.build(choice)
                except ValueError:
                    continue
            branch.advance()
            steps.append(
                PlanStep(
                    turn=branch.turn,
                    action="build" if choice else "wait",
                    building=choice,
                    treasury_after=branch.economy.treasury,
                    happiness_after=happiness_of(branch.placed),
                    population_after=branch.population,
                )
            )
            self._search(branch, depth + 1, steps, best)
            steps.pop()


def _clone(city: City) -> City:
    fresh = City(name=city.name, treasury=city.economy.treasury)
    fresh.placed = list(city.placed)
    fresh.turn = city.turn
    return fresh
