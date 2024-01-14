#!/usr/bin/python3
"""
Python Interpreter

The class module
"""

import json
"""The JSON module"""


class Base:
    """Instantiating the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a string to a file"""
        file_list = []
        if list_objs is not None:
            for obj in list_objs:
                file_list.append(obj.to_dictionary())
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(file_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_instance = Rectangle(1, 1)
        elif cls is Square:
            new_instance = Square(1)
        else:
            new_instance = None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """loads from a file and returns a list of instances"""
        from os import path
        filename = '{}.json'.format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            cls_str = f.read()
            list_instance = Base.from_json_string(cls_str)
            return [cls.create(**l) for l in list_instance]
