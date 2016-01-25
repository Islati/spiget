import spiget

if __name__ == "__main__":
    print("Retrieving Information about Spigot Releases")
    print(spiget.get_resources())

    print("Retrieving information on the Spigot Commons Release")
    print(spiget.get_resource('15290'))

    print("Retrieving Version 1.8.8-1 of Commons")
    print(spiget.get_resource("15290", version='1.8.8-1'))

    print("Retrieving the download link for Commons")
    print(spiget.get_resource_download('15290'))

    print("Retrieving the author for Commons")
    print(spiget.get_resource_author('15290'))

    print("Retrieving the latest resources")
    print(spiget.get_new_resources())

    print("Retrieving the categories of Resources")
    print(spiget.get_categories())

    print("Retrieving Sub Categories from Bukkit")
    print(spiget.get_categories('bukkit'))

    print("Retrieving Bukkit resources")
    print(spiget.get_category_resources('bukkit'))

    print("Getting Authors")
    print(spiget.get_authors())

    print("Retrieving newest Authors")
    print(spiget.get_new_authors())

    print("Retrieving details on MumbosHut")
    print(spiget.get_author_resources('MumbosHut'))

    print("Another shake for MumbosHut")
    print(spiget.get_author_details('MumbosHut'))

    print("Search Resources: Commons")
    print(spiget.search_resources('Commons'))

    print("Searching for authors")
    print(spiget.search_author('Mumbos'))
