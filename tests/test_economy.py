from tycoon_city.economy import Economy


def test_tax_income():
    econ = Economy()
    assert econ.tax_income(population=10, jobs=5) == 10 * 3 + 5 * 2


def test_tick_updates_treasury():
    econ = Economy(treasury=500)
    delta = econ.tick(population=10, jobs=0, placed=["house", "house"])
    assert econ.treasury == 500 + delta


def test_spend_rejects_overdraft():
    econ = Economy(treasury=50)
    try:
        econ.spend("factory")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_nightlife_bonus_applies_per_arcade():
    econ = Economy()
    without = econ.tax_income(population=0, jobs=0, arcades=0)
    with_two = econ.tax_income(population=0, jobs=0, arcades=2)
    assert with_two - without == 10
