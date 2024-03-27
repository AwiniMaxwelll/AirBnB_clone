#!/usr/bin/python3
"""The storage model for serialization of python string to json
and deserialization of json to python string"""

import json as js


class FileStorage:
    """
    Serialize instance to json file and deserialize json to string
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        set new obj into __objects
        """
        key = str(obj.__class__.__name___) + '.' + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes the objects into json file
        """
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='UTF8') as fd:
            js.dump(obj_dict, fd)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import BaseModel

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as fd:
                temp = js.load(fd)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
