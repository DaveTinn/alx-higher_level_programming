#!/usr/bin/python3
"""Python Interpreter."""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """Instantiation of a class Rectangle."""

    def __init__(self, size):
        """
        Defines the width and height of a class Rectangle.

        Arguments:
            size: Size of the Square.
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Implements the area."""
        return self.__size ** 2

    def __str__(self):
        return '[Rectangle] ' + str(self.__size) + '/' + str(self.__size)
