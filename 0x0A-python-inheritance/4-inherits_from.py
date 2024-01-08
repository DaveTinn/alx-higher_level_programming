#!/usr/bin/python3
"""Python Interpreter."""


def inherits_from(obj, a_class):
    """
    Retrieves an instance of a class inherited from a specific class.

    Arguments:
        obj: The object
        a_class: The type of class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
