#!/usr/bin/python3
"""Python Interpreter."""


class MyInt(int):
    """Instantiating a class inheritance."""

    def __new__(cls, *argmts, **k_argmts):
        """"Defines the new instance of the class."""
        return super().__new__(cls, *argmts, **k_argmts)
    def __eq__(self, invert):
        """Defines the equal == operator."""
        return int(self) != invert

    def __ne__(self, invert):
        """Defines the not equal != operator."""
        return int(self) == invert
