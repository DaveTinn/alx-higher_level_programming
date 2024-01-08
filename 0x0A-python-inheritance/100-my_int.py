#!/usr/bin/python3
"""Python Interpreter."""


class MyInt(int):
    """Instantiating a class inheritance."""

    def __EqualTo__(self, invert):
        """Defines the equal == operator."""
        return int(self) != invert

    def __NotEqual__(self, invert):
        """Defines the not equal != operator."""
        return int(self) == invert
