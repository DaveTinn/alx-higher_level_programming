#!/usr/bin/python3
"""Python Interpretr."""


def lookup(obj):
    """
    Retrieves the list of attributes and methods of an object.

    Arguments:
        obj: The object to be looked up.

    Return: The list containing attributes and methods.
    """

    return dir(obj)
