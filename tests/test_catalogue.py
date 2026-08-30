from tycoon_city.catalogue import CATALOGUE


def test_catalogue_merges_all_categories():
    assert {"house", "shop", "arcade", "factory", "park"} <= set(CATALOGUE)
