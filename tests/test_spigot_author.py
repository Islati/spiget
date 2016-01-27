from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from spiget import *

def test_spigot_author_from_username():
    author = SpigotAuthor.from_username("MumbosHut")
    assert author.username == "MumbosHut"
    assert author.id == 3629
    assert 15290 in author.resource_ids
    assert len(author.resources) > 0


def test_spigot_author_from_id():
    author = SpigotAuthor.from_id(3629)
    assert author.username == "MumbosHut"
    assert author.id == 3629
    assert 15290 in author.resource_ids
    assert len(author.resources) > 0