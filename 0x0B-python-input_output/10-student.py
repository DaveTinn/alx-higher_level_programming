#!/usr/bin/python3
"""
Python Interpreter

My class module
"""


class Student:
    """Instantiating a class Student"""

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
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
