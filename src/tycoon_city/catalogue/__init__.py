from tycoon_city.catalogue import civic, commercial, industrial, residential
from tycoon_city.catalogue.base import Building

CATALOGUE: dict[str, Building] = {
    **residential.BUILDINGS,
    **commercial.BUILDINGS,
    **industrial.BUILDINGS,
    **civic.BUILDINGS,
}

__all__ = ["Building", "CATALOGUE"]
