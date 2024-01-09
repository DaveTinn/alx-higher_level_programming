#!/usr/bin/python3
"""Python Interpreter."""


import json
"""The JSON module."""


def load_from_json_file(filename):
    """"Creates an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
