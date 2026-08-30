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


def test_projected_balance():
    econ = Economy(treasury=100)
    assert econ.projected_balance(per_turn_delta=10, turns=3) == 130


def test_is_solvent_false_when_bleeding():
    econ = Economy(treasury=10)
    assert econ.is_solvent(per_turn_delta=-5, turns=5) is False
