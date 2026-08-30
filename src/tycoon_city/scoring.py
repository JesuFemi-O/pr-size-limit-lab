"""Scoring helpers shared by the planner and the CLI report."""

from __future__ import annotations

from dataclasses import dataclass

WEIGHTS = {
    "population": 4.0,
    "jobs": 1.5,
    "happiness": 2.0,
    "treasury": 0.05,
}


@dataclass
class ScoreCard:
    population: float
    jobs: float
    happiness: float
    treasury: float

    @property
    def total(self) -> float:
        return self.population + self.jobs + self.happiness + self.treasury

    def as_rows(self) -> list[tuple[str, float]]:
        return [
            ("population", self.population),
            ("jobs", self.jobs),
            ("happiness", self.happiness),
            ("treasury", self.treasury),
            ("total", self.total),
        ]

    def render(self) -> list[str]:
        return [f"{name:>11}: {value:8.1f}" for name, value in self.as_rows()]


def score(population: int, jobs: int, happiness: int, treasury: int) -> ScoreCard:
    return ScoreCard(
        population=population * WEIGHTS["population"],
        jobs=jobs * WEIGHTS["jobs"],
        happiness=happiness * WEIGHTS["happiness"],
        treasury=treasury * WEIGHTS["treasury"],
    )


def grade(total: float) -> str:
    if total >= 400:
        return "A"
    if total >= 250:
        return "B"
    if total >= 120:
        return "C"
    return "D"


def compare(before: ScoreCard, after: ScoreCard) -> list[str]:
    out = []
    for (name, lhs), (_, rhs) in zip(before.as_rows(), after.as_rows()):
        out.append(f"{name:>11}: {lhs:8.1f} -> {rhs:8.1f} ({rhs - lhs:+.1f})")
    return out
