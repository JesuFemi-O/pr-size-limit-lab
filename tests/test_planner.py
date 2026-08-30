from tycoon.city import City
from tycoon.planner import Planner


def test_planner_returns_a_plan():
    plan = Planner(goal="growth", lookahead=2).plan(City(treasury=1200))
    assert plan.turns == 2
