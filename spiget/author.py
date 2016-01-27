from spiget import SpigotAuthorInitializeException, SpigotResource
from spiget.web import is_valid_author, get_author_details, get_author_resources


class SpigotAuthor(object):
    def __init__(self, id=None, username=None, json=None):
        self.json = None
        self.id = None
        self.username = None
        self.last_activity = None
        self.resources = []
        self.link = None

        if id is None and username is None and json is None:
            raise SpigotAuthorInitializeException(
                "Unable to create an author with no parameters; Either initialize with an id/name, or json of the authors details")

        if json is not None:
            self.json = json
            self.__configure_from_json(json)
            return

        if id is not None:
            if is_valid_author(id):
                self.id = id
            else:
                raise SpigotAuthorInitializeException("Unable to find an author with the id %s" % id)

        if username is not None:
            if is_valid_author(username):
                self.username = username
            else:
                raise SpigotAuthorInitializeException("Unable to find an author with the username %s" % username)

        if id is not None and username is not None:
            self.json = get_author_details(id)
        elif id is None and username is not None:
            self.json = get_author_details(username)
        elif id is not None and username is None:
            self.json = get_author_details(id)
        else:
            raise SpigotAuthorInitializeException("No variable available to initialize Author by; ID or Username.")

        self.__configure_from_json(self.json)

    def __configure_from_json(self, json):
        self.id = json['id']
        self.username = json['username']
        self.last_activity = json['lastActivity']
        resources = json['resources']
        if len(resources) > 0:
            for resource_id in resources:
                res = SpigotResource(resource_id=resource_id)
                self.resources.append(res)
                print("%s belongs to Author %s" % (res.name, self.username))

        self.link = json['link']

    @staticmethod
    def from_id(id):
        return SpigotAuthor(id=id)

    @staticmethod
    def from_username(username):
        return SpigotAuthor(username=username)

    @staticmethod
    def from_json(json):
        return SpigotAuthor(json=json)
