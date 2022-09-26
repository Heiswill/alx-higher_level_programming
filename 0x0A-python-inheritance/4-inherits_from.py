#!/usr/bin/python3
"""Define a function that inherits directly/indirect
from a specified class"""


def inherits_from(obj, a_class):
    """Check it object is an instance of a class that
    inherited directly/indirectly from a specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match.
    Returns:
        True: If object is instance of class, or False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
