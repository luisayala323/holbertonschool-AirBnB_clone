#!/usr/bin/python3
"""This module defines a class "FileStorage" that serializes and
deserializes instances to and from a JSON file."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A class to manage the storage of all our instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to our storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes our objects and saves them to a file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        class_mapping = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)

            for k, v in obj_dict.items():
                class_name = v['__class__']
                if class_name in class_mapping:
                    obj_class = class_mapping[class_name]
                    self.__objects[k] = obj_class(**v)
