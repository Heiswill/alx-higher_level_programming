#!/usr/bin/python3
"""Defines the Rectangle class."""
import sys
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set private attribute"""
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """get private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set private attribute."""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Get private attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set private attribute"""
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Get y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y attribute."""
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """Returns area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print to stdout the rectangle instance with the
        character '#'."""
        for i in range(self.height):
            [print('#', end="") for j in range(self.width)]
            print("")

    @staticmethod
    def setter_validation(attr, value):
        """ Validation for all setter methods.

        Args:
            value (int): attr to validate.

        Raises:
            TypeError: If input is not an integer.
            ValueError: If width/height is <= 0.
            ValueError: If x or y is < 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attr))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def __str__(self):
        """Over the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)


    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    def update(self, *args, **kwargs):
        """
        Assign each argument to an attribute.

        Args: Argument order is required.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass


