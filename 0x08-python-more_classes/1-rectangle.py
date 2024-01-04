#!/usr/bin/python3
"""Python Interpreter"""


class Rectangle:
    """Defines a type Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiating a instance of a class

        Variables:
            width: width of the Rectangle
            height: height of the Rectangle

        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self._width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value
