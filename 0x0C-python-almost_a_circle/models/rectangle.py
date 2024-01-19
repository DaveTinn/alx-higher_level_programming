#!/usr/bin/python3
"""
Python Interpreter

A class module
"""

from models.base import Base


class Rectangle(Base):
    """Instantiating the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Defining the instances of the class

        Arguments:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Defines the width of the class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the class Rectangle"""
        self.setter_validator('width', value, False)
        self.__width = value

    @property
    def height(self):
        """Defines the height of the class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the class Rectangle"""
        self.setter_validator('height', value, False)
        self.__height = value

    @property
    def x(self):
        """Defines the x-coordinate of the class Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Retrieves the x-coordinates"""
        self.setter_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Defines the x-coordinate of the class Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Retrieves the y-coordinate of the class Rectangle"""
        self.setter_validator('y', value)
        self.__y = value

    def setter_validator(self, name, value, positive=True):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if not positive and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
        elif positive and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
    def area(self):
        """Defines the area of the class Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle with character '#'."""
        for i in range(self.y):
            print()
        for idx in range(self.height):
            print(self.x * ' ' + self.width * '#')

    def __str__(self):
        """Defines the string method"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attributes"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for idx in range(len(args)):
            setattr(self, attrs[idx], args[idx])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictiinary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
