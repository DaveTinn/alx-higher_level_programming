#!/usr/bin/python3
"""Python Interpreter."""


def is_same_class(obj, a_class):
    """
    Determines if an object is an instance of the specified class.

    Arguments:
        obj: The object
        a_class: A type of class
    """
    return type(obj) == a_class
