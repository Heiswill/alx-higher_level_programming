#!/usr/bin/python3
"""Define a class square"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): the size of the square"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """returns the current square area"""
        area = self.__size ** 2
        return area
