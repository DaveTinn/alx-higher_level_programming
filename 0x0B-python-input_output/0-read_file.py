#!/usr/bin/python3
"""Python Interpreter."""


def read_file(filename=""):
    """Reads a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
