from minicity.city import City
from minicity.planner import Planner


def test_planner_returns_a_plan():
    plan = Planner(goal="growth", lookahead=2).plan(City(treasury=1200))
    assert plan.turns == 2
