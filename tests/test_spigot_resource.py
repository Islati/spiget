from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import pytest

from spiget import get_resource, SpigotResource, SpigotResourceException


def test_resource_from_json():
    resource = SpigotResource.from_json(json=get_resource(15290))
    assert resource is not None
    assert resource.name == 'Commons'
    assert resource.resource_id == 15290
    assert resource.author_name == "MumbosHut"
    assert resource.external is False


def test_resource_by_id():
    resource = SpigotResource.from_id(15290)
    assert resource is not None
    assert resource.name == 'Commons'
    assert resource.resource_id == 15290
    assert resource.author_name == "MumbosHut"
    assert resource.external is False


def test_invalid_resource():
    assert SpigotResource.from_name("_djfkjl4kj24242") is None


def test_resource_by_name():
    resource = SpigotResource.from_name("Commons")
    assert resource is not None
    assert resource.name == 'Commons'
    assert resource.resource_id == 15290
    assert resource.author_name == "MumbosHut"
    assert resource.external is False


def test_resource_external():
    resource = SpigotResource.from_id(15441)
    assert resource is not None
    assert resource.name == 'Craft Build Tools - Project Management Suite'
    assert resource.external is True
