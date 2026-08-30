from tycoon.city import City


def test_build_adds_population():
    city = City(treasury=1000)
    city.build("house")
    assert city.population == 4


def test_advance_increments_turn():
    city = City()
    city.advance()
    assert city.turn == 1


def test_summary_keys():
    city = City()
    assert set(city.summary()) == {
        "name",
        "turn",
        "population",
        "jobs",
        "treasury",
        "buildings",
    }

def test_net_worth_includes_buildings():
    c = City(treasury=1000)
    c.build("house")
    assert c.net_worth() == 1000
