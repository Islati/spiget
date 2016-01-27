# Spiget - Python Interface

This python implementation of the Spiget.org API has been designed to be extremely easy and intuitive to use, working with whichever style you prefer (Json, or Objects) and provides all the functionality available in each choice of method.


**How to install**

```
pip install spiget
```

**Feature list**:

 * All methods of the Spiget.org API included
 * Direct access to JSON via method calls
 * Classes / Objects representing different API resources
 * Easy to use, fast, simple, and clean.

Here's a quick set of examples of how easy the Spiget API Is, and what it's capable of! :+1:

```python
from spiget import *

# Check if there's a resource available with a specific name
if is_valid_resource("Commons):
	#Execute your code here

#You can also operate on resources via their ID 
#(15290 is Commons, as above)
if is_valid_resource(15290):
	#Execute your code here.
    
#Get resource retrieves the JSON Details for a specific resurce
json = get_resource("Commons")

#Same as above
json = get_resource(15290)

#Let's see this output!
print(json)

#Below is the result of retrieving the "Commons" Resource, above!
{
'external': False,
'category': {'id': 26}, 
'link': 'https://www.spigotmc.org/resources/15290', 
'lastUpdate': 'Dec 15, 2015 at 9:35 PM', 
'id': 15290, 
'download': 'https://www.spigotmc.org/resources/commons.15290/download?version=58055',
'author': {
	'id': 3629
 },
 'versions': ['1.8.8', '1.8.8-1', '1.8.8-2'],
 'version': '1.8.8-2',
 'tag': 'An all in one Framework (API) providing the Essentials for server owners, and developers!',
 'icon': '',
 'file': {
 	'size': '1 MB',
    'type': '.jar'
  },
  'name': 'Commons'
}

#Here's how to achieve the same thing with an Object!
resource = SpigotResource.from_id(15290)
#or
resource = SpigotResource.from_name("Commons")
#or even from json directly!
resource = SpigotResource.from_json(get_resource("Commons"))

#Not calling one of the static methods, and initializing the object
#directly requires JSON to be passed.
resource = SpigotResource(get_resource(15290))

#Printing will print the same data as previously..

#Lets get an author!
author = SpigotAuthor.from_username("MumbosHut")

#How about a category?!
category = SpigotCategory.from_id(4)
```

*Note: For all available methods, and features view the [source code](https://github.com/TechnicalBro/spiget/blob/master/spiget/__init__.py)*

**If you have a feature suggestion: Open an issue, or submit a pull request**

Happy coding! :D <3
