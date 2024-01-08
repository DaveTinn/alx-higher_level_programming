#!/usr/bin/python3
"""Python Interpreter."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation of a class Rectangle."""

    def __init__(self, width, height):
        """
        Defines the width and height of a class Rectangle.

        Arguments:
            width: The width of the Rectangle.
            height: The height of the Rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implements the area."""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
