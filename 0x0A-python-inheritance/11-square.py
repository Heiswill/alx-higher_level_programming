#!/usr/bin/python3
"""Defines a Square class that extends a Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''print'''
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
