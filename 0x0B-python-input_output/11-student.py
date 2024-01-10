#!/usr/bin/python3
"""
Python Interpreter

My class module
"""


class Student:
    """Instantiating the class Student."""

    def __init__(self, first_name, last_name, age):
        """
        Defines the instances of the class Student

        Arguments:
            self: The reference to the instance attributes
            first_name: The first nstance attibute
            last_name: The second instance attribute
            age: The third instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of the class instance"""
        try:
            if type(attr) is not str:
                return self.__dict__
        except Exception:
            return self.__dict__
        new_attrs = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_arrts[key] = value
        return new_attrs

    def reload_from_json(self, json):
        """Replaces all attributes of the class instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
