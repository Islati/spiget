import requests

__config = {
    'domain': 'http://api.spiget.org',
    'version': 'v1',
    'userAgent': 'Spiget-PythonAPI/0.0.1',
}


def __build_api_url():
    return "%s/%s" % (__config['domain'], __config['version'])


def __get_header_dict():
    return {'user-agent': __config['userAgent']}


def get_api_url(uri):
    url = "%s/%s" % (__build_api_url(), uri)
    return url


def get_resources(size=100):
    r = requests.get(get_api_url('resources/'), params={"size": size}, headers=__get_header_dict())
    return r.json()


def get_resource(id, version=None):
    r = None
    if version is not None:
        r = requests.get(get_api_url('resources/%s/versions/%s' % (id, version)), headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('resources/%s' % id), headers=__get_header_dict())

    return r.json()


def get_resource_name(id):
    r = requests.get(get_api_url('resources/%s' % id), headers=__get_header_dict())
    return r.json()['name']


def get_resource_versions(id):
    r = requests.get(get_api_url('resources/%s/versions' % id), headers=__get_header_dict())
    return r.json()


def get_resource_latest_version(id):
    versions = get_resource_versions(id)
    version_ids = {}
    for version in versions:
        link = version['download']
        link_version = link.split("?version=", 1)[1]
        version_ids[version['version']] = (int(link_version))

    max_key = max(version_ids, key=version_ids.get)
    return max_key


def get_resource_download(id, version="latest"):
    v_id = None

    if version == "latest":
        v_id = get_resource_latest_version(id)
    else:
        v_id = version

    versions = get_resource_versions(id)
    link = None
    for version in versions:
        if version['version'] != str(v_id):
            continue
        link = version['download']
        break

    return link


def get_resource_author(id):
    r = requests.get(get_api_url('resources/%s/author' % id), headers=__get_header_dict())
    return r.json()


def get_new_resources(size=25):
    r = requests.get(get_api_url('resources/new'), params={"size": size}, headers=__get_header_dict())
    return r.json()


def get_categories(sub_category=""):
    r = requests.get(get_api_url('categories/%s' % sub_category), headers=__get_header_dict())
    return r.json()


def get_category_name(id):
    return get_categories(id)['name']


def get_category_resources(category, size=None):
    r = None
    if size is not None and size > 0:
        r = requests.get(get_api_url('categories/%s/resources' % category), params={"size": size},
                         headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('categories/%s/resources' % category), headers=__get_header_dict())
    return r.json()


def get_authors(size=None):
    r = None
    if size is not None and size > 0:
        r = requests.get(get_api_url('authors'), params={'size': size}, headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('authors'), headers=__get_header_dict())

    return r.json()


def get_author_details(id):
    r = requests.get(get_api_url('authors/%s' % id), headers=__get_header_dict())
    return r.json()


def get_author_resources(id):
    r = requests.get(get_api_url('authors/%s/resources' % id), headers=__get_header_dict())
    return r.json()


def get_new_authors(size=None):
    r = None
    if size is not None:
        r = requests.get(get_api_url('authors/new'), params={"size": size}, headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('authors/new'), headers=__get_header_dict())

    return r.json()


def search_resources(query, field=None):
    r = None
    if field is not None:
        r = requests.get(get_api_url('search/resources/%s/%s' % (query, field)), headers=__get_header_dict())
    else:
        r = requests.get(get_api_url('search/resources/%s' % query), headers=__get_header_dict())
    return r.json()


def search_author(query):
    r = requests.get(get_api_url('search/authors/%s' % query), headers=__get_header_dict())
    return r.json()


def is_valid_resource(resource_id):
    json = get_resource(resource_id)
    return 'name' in json and 'id' in json


def is_valid_author(id):
    return 'username' in get_author_details(id)


class SpigotResource(object):
    def __init__(self, json):
        self.name = None
        self.tag = None
        self.last_update = None
        self.author_id = None
        self.download = None
        self.link = None
        self.version = None
        self.versions = []
        self.category = None
        self.external = False
        self.file_size = ""
        self.file_type = ""
        self.json = json

        self.__configure_from_json(self.json)

    def __configure_from_json(self, json):
        self.resource_id = json['id']
        self.name = json['name']
        self.tag = json['tag']
        self.last_update = json['lastUpdate']
        self.author_id = json['author']['id']
        self.author_name = get_author_details(self.author_id)['username']
        # TODO find way to get author object inside resource
        self.download = json['download']
        self.link = json['link']
        self.version = json['version']
        self.versions = []
        # Iterate through all the versions available and append it to the objects available versinos
        for version in json['versions']:
            self.versions.append(version)

        self.category_id = json['category']['id']

        self.external = json['external']

        self.file_size = ""
        self.file_type = ""
        if not self.external:
            self.file_size = json['file']['size']
            self.file_type = json['file']['type']

    def get_download_link(self, version="latest"):
        return get_resource_download(self.resource_id, version)

    @staticmethod
    def from_json(json):
        return SpigotResource(json)

    @staticmethod
    def from_id(id):
        if is_valid_resource(id) is False:
            return None

        return SpigotResource(get_resource(id))

    @staticmethod
    def from_name(name):
        if is_valid_resource(name) is False:
            return None

        return SpigotResource(get_resource(name))


class SpigotCategory(object):
    def __init__(self, id, name=None):
        self.category_id = id
        self.subcategories = []
        self.__retrieve_parent = True
        self.parent_category = None
        self.name = None

        if name is None:
            self.name = get_category_name(id)
        else:
            self.name = name

    def has_subcategories(self):
        if self.subcategories is None:
            return False
        elif len(self.subcategories) == 0:
            self.get_subcategories()

        return len(self.subcategories) > 0

    def has_parent_category(self):
        if self.__retrieve_parent is False:
            return False

        category_json = get_categories(self.category_id)
        if 'parent' not in category_json:
            self.__retrieve_parent = False
            return False
        else:
            self.__retrieve_parent = False
            self.parent_category = SpigotCategory(category_json['id'], name=category_json['name'])
            return True

    def get_subcategories(self):
        if self.subcategories is None:
            return None

        if len(self.subcategories) == 0:
            category_json = get_categories(self.category_id)

            if "childs" not in category_json:
                self.subcategories = None
                return self.subcategories

            if "error" in category_json:
                raise SpigotCategoryException(
                    "Unable to retrieve subcategories for category %s (id: %s)" % (self.category_id, self.name))

            for category in category_json['childs']:
                resource_category = SpigotCategory(id=category)
                print("%s has a subcategory of %s (id: %s)" % (
                    self.name,
                    resource_category.name,
                    resource_category.category_id
                ))

                self.subcategories.append(resource_category)

            print("%s has %s subcategories" % (self.name, len(self.subcategories)))

        return self.subcategories

    def get_parent_category(self):
        if self.has_parent_category() is True:
            return self.parent_category
        else:
            return None

    def get_resources(self, max=10):
        resources = []
        for category_resource in get_category_resources(self.category_id, size=max):
            try:
                resources.append(SpigotResource.from_id(category_resource['id']))
            except SpigotResourceException as e:
                continue

        return resources

    @staticmethod
    def from_id(id):
        return SpigotCategory(id=id)


class SpigotAuthor(object):
    def __init__(self, json):
        self.json = None
        self.id = None
        self.username = None
        self.last_activity = None
        self.resources = []
        self.resource_ids = []
        self.link = None
        self.json = json

        self.__configure_from_json(self.json)

    def __configure_from_json(self, json):
        self.id = json['id']
        self.username = json['username']
        self.last_activity = json['lastActivity']
        resources = json['resources']
        if len(resources) > 0:
            for res in resources:
                self.resource_ids.append(res)
                self.resources.append(SpigotResource.from_id(res))

        self.link = json['link']

    @staticmethod
    def from_id(id):
        return SpigotAuthor(get_author_details(id))

    @staticmethod
    def from_username(username):
        return SpigotAuthor(get_author_details(username))

    @staticmethod
    def from_json(json):
        return SpigotAuthor(json=json)


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

    if id is None and username is None:
        raise SpigotAuthorException("Unable to retrieve an Author without an Identifier")

    if id is None:
        return SpigotAuthor.from_username(username)
    else:
        return SpigotAuthor.from_id(id)


class SpigotResourceException(Exception):
    pass


class SpigotAuthorException(Exception):
    pass


class SpigotCategoryException(Exception):
    pass
