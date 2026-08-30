import pytest

from tycoon import buildings


def test_catalogue_names_sorted():
    assert buildings.names() == sorted(buildings.names())


def test_get_known():
    assert buildings.get("house").population == 4


def test_get_unknown():
    with pytest.raises(ValueError):
        buildings.get("castle")


def test_library_in_catalogue():
    assert buildings.get("library").jobs == 3
