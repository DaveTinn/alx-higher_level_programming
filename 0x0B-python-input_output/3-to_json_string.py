#!/usr/bin/python3
"""Python Interpreter."""


import json
"""The JSON module."""


def to_json_string(my_obj):
    """
    Defines the JSON representation of an obj.

    Arguments:
        my_obj (str): The object to be represented.
    """
    return json.dumps(my_obj)
