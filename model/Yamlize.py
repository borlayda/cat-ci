"""
 This object is for serializing objects to yaml files.
"""

import yaml

class Yamlize(object):

    def __init__(self, name):
        self.name = name

    def save(self):
        """
        This method serialize the object to the file
        described by the name of the object.
        """
        serialized_object = yaml.dump(self)
        with open("yaml/"+self.name + '.yaml', 'w+') as serialize_file:
            serialize_file.write(str(serialized_object))

    def load(self, filename):
        """
        This method deserialize the object from a file
        described by filename parameter.
        @param filename: Name of the serialized file
        @type filename: str
        """
        with open("yaml/"+filename, 'r+') as serialize_file:
            self = yaml.load(serialize_file.read())
