from tycoon_city.city import City


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


def test_happiness_drops_with_factories():
    city = City(treasury=10_000)
    city.build("factory")
    assert city.happiness < 50


def test_report_includes_happiness():
    city = City()
    assert any("happiness" in line for line in city.report())
