#!/usr/bin/python3
'''Python Interpreter.'''


class Square:
    '''Defines a class Square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Instantiating an instance of the Square class.

        Arguments:
            size: size of the square
            position: position of the isquare.
        Raise:
            TypeError: if size is not an integer.
            ValueError: size is less than zero.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Property to retrieve the size of instance attribute.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Property setter to set the size of instance attribute.'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''Property to retrieve the position of instance attribute.'''
        return (self.position)

    @position.setter
    def position(self, value):
        '''Property setter to set the position of instance attribute.
        Raise:
            TypeError: if not a tuple of two positive integers
        '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(dgt, int) for dgt in value) or
                any(dgt < 0 for dgt in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''Returns the current square area.'''
        return (self.__size ** 2)

    def my_print(self):
        '''Prints the square with a character #.'''
        if self.__size == 0:
            print("")
            return

        [print("") for idx in range(0, self.__position[1])]
        for idx in range(self.size):
            [print(" ", end="") for d in range(0, self.__position[0])]
            [print("#", end="") for x in range(0, self.__size)]
            print()
