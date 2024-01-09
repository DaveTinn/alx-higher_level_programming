#!/usr/bin/python3
"""Python Interpreter."""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object.

    Arguments:
        obj: The object to add the attribute.
        attr: The attribute
        value: The value to set for the attribute.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(obj, attr, value)
