"""Named build strategies the planner can be pointed at."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Strategy:
    key: str
    goal: str
    lookahead: int
    note: str

    def as_row(self) -> tuple[str, str, int, str]:
        return (self.key, self.goal, self.lookahead, self.note)


STRATEGIES: dict[str, Strategy] = {
    "turtle": Strategy("turtle", goal="profit", lookahead=5, note="hoard cash, build slowly"),
    "boomtown": Strategy("boomtown", goal="growth", lookahead=4, note="maximise population fast"),
    "resort": Strategy("resort", goal="happy", lookahead=4, note="parks and arcades first"),
    "workshop": Strategy("workshop", goal="jobs", lookahead=4, note="factories and shops first"),
    "balanced": Strategy("balanced", goal="balanced", lookahead=3, note="no strong preference"),
}


def get(key: str) -> Strategy:
    try:
        return STRATEGIES[key]
    except KeyError:
        raise ValueError(f"unknown strategy: {key!r}") from None


def keys() -> list[str]:
    return sorted(STRATEGIES)


def recommend(population: int, treasury: int, happiness: int) -> Strategy:
    if treasury < 200:
        return STRATEGIES["turtle"]
    if happiness < 40:
        return STRATEGIES["resort"]
    if population < 8:
        return STRATEGIES["boomtown"]
    return STRATEGIES["balanced"]


def describe_all() -> list[str]:
    rows = ["key        goal      lookahead  note"]
    for strategy in STRATEGIES.values():
        rows.append(
            f"{strategy.key:<10} {strategy.goal:<9} {strategy.lookahead:<10} {strategy.note}"
        )
    return rows
