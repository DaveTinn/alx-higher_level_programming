#!/usr/bin/python3
"""Python Interpreter."""


import json
""""The JSON module."""


def save_to_json_file(my_obj, filename):
    """Saves an Object to a text file using a JSON reepresentation."""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
