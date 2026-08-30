from minicity.city import City


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

# covered by v0.2.0 release verification
