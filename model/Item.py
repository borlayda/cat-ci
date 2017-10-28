"""
 Common item class for serializing and saving objects into
 database.
"""

from Yamlize import Yamlize
from DatabaseBuilder import DatabaseBuilder

class Item(Yamlize):

    def __init__(self, name, description = ""):
        super(Item, self).__init__(name)
        self.description = description
        self.db = DatabaseBuilder()
