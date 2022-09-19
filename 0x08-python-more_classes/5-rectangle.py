#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Raises:
            TypeError: If width/height is not integer.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int) or
        isinstance(self.__height, bool):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self._-height) + ")"
        return (rect)

    def __del__(self):
        """Deletes an instance of Rectangle class, and prints "bye"
            message
        """
        print("Bye rectangle...")
