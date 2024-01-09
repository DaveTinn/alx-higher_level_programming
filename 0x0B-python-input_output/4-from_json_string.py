#!/usr/bin/python3
"""Python Interpreter."""


import json
"""The JSON module."""

def from_json_string(my_str):
    """Defines the JSON string representation of an object.
    Aguments:
        my_str (str): The JSON string.
    """
    return json.loads(my_str)
