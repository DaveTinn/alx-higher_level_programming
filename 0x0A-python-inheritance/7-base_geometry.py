#!/usr/bin/python3
"""Python Interpreter."""


class BaseGeometry:
    """Instantiating a class BaseGeometry."""

    def area(self):
        """
        Defines the area.

        Raises:
            TypeError: If area is not implemented.
        """
        raise TypeError('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Defines the validation of value.

        Arguments:
            name (str): The name of the value to be validated
            value: The value to be validated

        Raises:
            TypeError: If value is an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
