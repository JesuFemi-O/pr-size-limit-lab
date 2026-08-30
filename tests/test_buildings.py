import pytest

from tycoon_city import buildings


def test_catalogue_names_sorted():
    assert buildings.names() == sorted(buildings.names())


def test_get_known():
    assert buildings.get("house").population == 4


def test_get_unknown():
    with pytest.raises(ValueError):
        buildings.get("castle")


def test_category_known():
    assert buildings.category("factory") == "industrial"


def test_category_unknown_raises():
    with pytest.raises(ValueError):
        buildings.category("castle")


def test_describe_mentions_category():
    assert "commercial" in buildings.describe("shop")
