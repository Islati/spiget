from spiget import SpigotCategoryException, SpigotResource, SpigotResourceInitializeException
from spiget.web import get_category_name, get_categories, get_category_resources


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
                resources.append(SpigotResource(resource_id=category_resource['id']))
            except SpigotResourceInitializeException as e:
                continue

        return resources
