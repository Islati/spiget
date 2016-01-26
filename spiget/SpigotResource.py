import spiget


class SpigotResourceException(Exception):
    pass


class SpigotResource(object):
    def __init__(self, resource_id=None, json=None):
        if resource_id is None and json is None:
            raise SpigotResourceException("Unable to initialize spigot resource with no arguments")

        if json is not None:
            if 'id' in json:
                self.resourceid = json['id']

            if 'name' in json:
                self.name = json['name']

            if 'tag' in json:
                self.name = json['tag']

            if 'lastUpdate' in json:
                self.last_update = json['lastUpdate']
            pass

        if not spiget.is_valid_resource(resource_id):
            raise SpigotResourceException('Invalid Spigot Resource id(%s)' % resource_id)

        # todo check if resource id is int
        if isinstance(resource_id, str):
            if not resource_id.isdigit():
                self.name = resource_id
            else:
                self.resourceid = resource_id
        elif isinstance(resource_id, int):
            self.resourceid = resource_id
        else:
            raise SpigotResourceException(
                'Unable to intialize a resource with %s as the ID; Requires a resource name, or ID.' % resource_id)
