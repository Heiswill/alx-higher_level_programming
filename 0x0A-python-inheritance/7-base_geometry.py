#!/usr/bin/python3
"""Defines an BaseGeometry class."""


class BaseGeometry:
    """Add public instance methods."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates `value`.
        Args:
            name (str): Argument name.
            value (int): Argument to validate.
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
