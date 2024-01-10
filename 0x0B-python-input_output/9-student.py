#!/usr/bin/python3
"""
Python Interpreter

My class module
"""


class Student:
    """Instantiating class Student."""

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

    def to_json(self):
        """Retrieves the dictionary representatioon of the class."""
        return self.__dict__
