#!/usr/bin/python3
"""Python Interpreter."""


import sys
"""The sys module."""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_args = list(sys.argv[1:])

try:
    existing_args = load_from_json_file("add_item.json")
except Exception:
    existing_args = []

existing_args.extend(new_args)
save_to_json_file(existing_args, "add_item.json")
