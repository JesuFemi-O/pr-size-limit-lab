import pytest

from minicity import buildings


def test_catalogue_names_sorted():
    assert buildings.names() == sorted(buildings.names())


def test_get_known():
    assert buildings.get("house").population == 4


def test_get_unknown():
    with pytest.raises(ValueError):
        buildings.get("castle")

def test_costliest_is_factory():
    assert buildings.costliest() == "factory"
