"""Cheap straight-line and moving-average treasury forecasts."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import fmean


@dataclass
class Forecast:
    horizon: int
    values: list[int]

    @property
    def final(self) -> int:
        return self.values[-1] if self.values else 0

    @property
    def lowest(self) -> int:
        return min(self.values) if self.values else 0

    @property
    def goes_negative(self) -> bool:
        return any(v < 0 for v in self.values)

    def first_negative_turn(self) -> int | None:
        for i, v in enumerate(self.values, start=1):
            if v < 0:
                return i
        return None

    def as_rows(self) -> list[tuple[int, int]]:
        return list(enumerate(self.values, start=1))


def straight_line(treasury: int, per_turn_delta: int, horizon: int) -> Forecast:
    values: list[int] = []
    running = treasury
    for _ in range(horizon):
        running += per_turn_delta
        values.append(running)
    return Forecast(horizon=horizon, values=values)


def compounding(treasury: int, rate: float, horizon: int) -> Forecast:
    values: list[int] = []
    running = float(treasury)
    for _ in range(horizon):
        running *= 1.0 + rate
        values.append(round(running))
    return Forecast(horizon=horizon, values=values)


def moving_average(history: list[int], window: int = 3) -> float:
    if not history:
        return 0.0
    window = min(window, len(history))
    return fmean(history[-window:])


def blended(treasury: int, history: list[int], horizon: int, window: int = 3) -> Forecast:
    deltas = _deltas(history)
    delta = round(moving_average(deltas, window)) if deltas else 0
    return straight_line(treasury, delta, horizon)


def _deltas(history: list[int]) -> list[int]:
    return [b - a for a, b in zip(history, history[1:])]
