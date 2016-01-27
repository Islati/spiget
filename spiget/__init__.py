from spiget import web
from spiget.author import SpigotAuthor
from spiget.category import SpigotCategory
from spiget.resource import SpigotResource

get_api_url = web.get_api_url
# All functions for interactions with Resources via JSON
get_resources = web.get_resources
get_resource = web.get_resource
get_resource_name = web.get_resource_name
get_resource_versions = web.get_resource_versions
get_resource_latest_version = web.get_resource_latest_version
get_resource_download = web.get_resource_download
get_resource_author = web.get_resource_author
get_new_resources = web.get_new_resources
search_resources = web.search_resources
is_valid_resource = web.is_valid_resource

# All functions for interacting with categories via JSON
get_categories = web.get_categories
get_category_name = web.get_category_name
get_category_resources = web.get_category_resources

# All functions for interacting with Authors via JSON
get_authors = web.get_authors
get_author_details = web.get_author_details
get_author_resources = web.get_author_resources
get_new_authors = web.get_new_authors
search_author = web.search_author
is_valid_author = web.is_valid_author


def retrieve_resource(id_or_name):
    """
    Retrieve a SpigotResource via its id, or name.

    Will raise an exception if unable to retrieve a resource via the given id, or name.
    :param id_or_name: The integer id, or name string
    :raises SpigotResourceInitializeException
    :return: SpigotResource with all possible data initialized.
    """
    return SpigotResource(id_or_name)


def retrieve_author(id=None, username=None):
    """
    Retrieve a SpigotAuthor via their id, or username.
    :param id:
    :param username:
    :return:
    """
    return SpigotAuthor(id=id, username=username)


class SpigotResourceException(Exception):
    pass


class SpigotResourceInitializeException(SpigotResourceException):
    pass


class SpigotAuthorException(Exception):
    pass


class SpigotAuthorInitializeException(SpigotAuthorException):
    pass


class SpigotCategoryException(Exception):
    pass
