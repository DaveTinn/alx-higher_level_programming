#!/usr/bin/python3
"""Python Interpreter."""


class Rectangle:
    """Defines a type Rectangle."""

    def __init__(self, width=0, height=0):
        """Instantiating an instance of a class Rectangle.

        Variables:
            width: width of a Rectangle
            height: height of a Rectangle

        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0.
        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Retrieves the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        rectangle_string = ""
        if self.__width != 0 or self.__height != 0:
            rectangle_string += '\n'.join(
                    '#' * self.__width for idx in range(self.__height))
        return rectangle_string
