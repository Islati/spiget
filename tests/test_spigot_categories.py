from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from spiget import *


def test_spigot_categories():
    category = SpigotCategory.from_id(4)
    assert category.category_id == 4
    assert category.name.lower() == "Bukkit".lower()
    assert category.has_subcategories()
    assert len(category.get_resources(5)) == 5
