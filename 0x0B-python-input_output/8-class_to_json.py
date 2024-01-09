#!/usr/bin/python3
"""Python Interpreter

My class module.
"""


def class_to_json(obj):
    """
    Defines a function that returns the description
    with simple data sructure list for JSON serialization
    of an object.
    """
    return obj.__dict__
