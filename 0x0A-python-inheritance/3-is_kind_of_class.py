#!/usr/bin/python3
"""Define an inheritance class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class,
    or an instance of a class that inherited from a specified
    class
    Args:
        obj (any): The obj to check.
        a_class (class): The class to match.
    Returns:
        Bool
    """
    return isinstance(obj, a_class)
