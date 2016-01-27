from spiget import *


class SpigotResource(object):
    def __init__(self, resource_id=None, name=None, json=None):
        self.name = None
        self.tag = None
        self.last_update = None
        self.author = None
        self.download = None
        self.link = None
        self.version = None
        self.versions = []
        self.category = None
        self.external = False
        self.file_size = ""
        self.file_type = ""
        self.json = None

        if resource_id is None and name is None and json is None:
            raise SpigotResourceInitializeException(
                "Unable to initialize a resource with no parameters; Must either set resource_id as a(n) resource id/name, or assign json as a collection of resource values")

        if resource_id is not None and name is None:
            if not is_valid_resource(resource_id):
                raise SpigotResourceException("Invalid resource ID (%s)" % resource_id)

            self.json = get_resource(resource_id)
        elif resource_id is None and name is not None:
            if not is_valid_resource(name):
                raise SpigotResourceInitializeException

            self.json = get_resource(name)
        else:
            self.json = get_resource(resource_id)

        if json is not None:
            self.json = json
        else:
            self.json = get_resource(resource_id)

        self.__configure_from_json(self.json)

    def __configure_from_json(self, json):
        self.resource_id = json['id']
        self.name = json['name']
        self.tag = json['tag']
        self.last_update = json['lastUpdate']
        self.author = SpigotAuthor(author=json['author']['id'])  # Intialize author object for resource.
        self.download = json['download']
        self.link = json['link']
        self.version = json['version']
        self.versions = []
        # Iterate through all the versions available and append it to the objects available versinos
        for version in json['versions']:
            self.versions.append(version)

        self.category = SpigotCategory(id=json['category']['id'])

        if 'external' in json['external']:
            self.external = json['external']
        else:
            self.external = False

        self.file_size = ""
        self.file_type = ""
        if not self.external:
            self.file_size = json['file']['size']
            self.file_type = json['file']['type']

    def get_download_link(self, version="latest"):
        return get_resource_download(self.resource_id, version)

    @staticmethod
    def from_json(json):
        return SpigotResource(None, json)

    @staticmethod
    def from_id(id):
        if not is_valid_resource(id):
            return None

        return SpigotResource(resource_id=id)

    @staticmethod
    def from_name(name):
        return SpigotResource.from_id(name)
