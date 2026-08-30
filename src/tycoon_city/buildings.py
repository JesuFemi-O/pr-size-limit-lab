"""Building catalogue for the toy city (now backed by the catalogue package)."""

from tycoon_city.catalogue import CATALOGUE, Building

__all__ = ["Building", "CATALOGUE", "get", "names"]


def get(name: str) -> Building:
    try:
        return CATALOGUE[name]
    except KeyError:
        raise ValueError(f"unknown building: {name!r}") from None


def names() -> list[str]:
    return sorted(CATALOGUE)
