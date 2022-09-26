#!/usr/bin/python3
"""Defines a Square class that extends a Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "size", self.__size)

    def area(self):
        return self.__size ** 2
