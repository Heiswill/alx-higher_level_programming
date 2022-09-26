#!/usr/bin/python3
"""Create a class Myclist to inherit from list"""


class MyList(list):
    """Extending built-in classes"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
