#!/usr/bin/python3
"""Python Interpreter."""


class MyInt(int):
    """Instantiating a class inheritance."""

    def __new__(cls, *args, **kwargs):
        """"Defines the new instance of the class."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, invert):
        """Defines the equal == operator."""
        return int(self) != invert

    def __ne__(self, invert):
        """Defines the not equal != operator."""
        return int(self) == invert
