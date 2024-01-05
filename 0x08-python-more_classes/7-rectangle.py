#!/usr/bin/python3
"""Python Interpreter."""


class Rectangle:
    """Defines a class Rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Instantiating an instance of a class Rectangle.

        Arguments:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        """Prints the Rectangle with characters."""
        if self.width == 0 and self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Deletes an instance of a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
