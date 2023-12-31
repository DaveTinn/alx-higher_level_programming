#!/usr/bin/python3
"""Python Interpreter"""


class Rectangle:
    """Defines a type Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiating a instance of a class

        Arguments:
            width: width of the Rectangle
            height: height of the Rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
