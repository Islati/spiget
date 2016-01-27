from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import spiget
import pytest


def test_get_resources():
    resources = spiget.get_resources(20)
    assert len(resources) == 20


def test_get_resource():
    commons = spiget.get_resource('15290')
    assert commons['name'].lower() == 'commons'
    assert commons['author']['id'] == 3629
    assert commons['id'] == 15290


def test_get_specific_version():
    commons = spiget.get_resource('15290', version='1.8.8-2')
    assert commons['version'] == '1.8.8-2'


def test_get_version_download_link():
    latest = spiget.get_resource_latest_version('15290')
    download_url = spiget.get_resource_download('15290')
    assert 'commons.15290' in download_url


def test_get_version_download_link_version_specific():
    download_url = spiget.get_resource_download('15290', version='1.8.8-1')
    assert download_url is not None
    assert download_url == "https://www.spigotmc.org/resources/commons.15290/download?version=56780"


def test_get_resource_author():
    author = spiget.get_resource_author('15290')
    assert author['id'] == 3629
    assert author['username'] == 'MumbosHut'
    assert 15290 in author['resources']
    assert author['link'] == 'https://www.spigotmc.org/members/3629'


def test_get_new_resources():
    new_resources = spiget.get_new_resources()
    assert len(new_resources) > 0


def test_get_categories():
    categories = spiget.get_categories()
    assert len(categories) > 0


def test_get_category_specific_information():
    bukkit_category = spiget.get_categories('bukkit')
    assert bukkit_category['id'] == 4

    for i in range(14, 18):
        assert i in bukkit_category['childs']

    for i in range(22, 26):
        assert i in bukkit_category['childs']


def test_get_category_resources():
    bukkit_category_resources = spiget.get_category_resources('bukkit', 5)
    assert len(bukkit_category_resources) == 5


def test_get_authors():
    authors = spiget.get_authors(10)
    assert len(authors) == 10


def test_get_author_details():
    mumbos_hut = spiget.get_author_details('MumbosHut')
    assert mumbos_hut['id'] == 3629
    assert 15290 in mumbos_hut['resources']
    assert mumbos_hut['username'] == 'MumbosHut'
    assert mumbos_hut['link'] == 'https://www.spigotmc.org/members/3629'


def test_get_author_resources():
    mumbos_hut_resources = spiget.get_author_resources('MumbosHut')
    valid_ids = [15441, 15290, 15706]
    for resource in mumbos_hut_resources:
        assert resource['id'] in valid_ids


def test_get_new_authors():
    new_authors = spiget.get_new_authors(10)
    assert len(new_authors) > 0


def test_resource_search():
    queried = spiget.search_resources('Commons')
    assert 'error' not in queried
    for resource in queried:

        if resource['name'].lower() == "commons":
            assert resource['id'] == 15290

    queried = spiget.search_resources("fdsfhsdfsdflsdjfs")
    assert 'error' in queried.keys()
    assert 'no resource found' in queried.values()


def test_author_search():
    queried = spiget.search_author('md_5')
    assert any('md_5' in key['username'] for key in queried)
