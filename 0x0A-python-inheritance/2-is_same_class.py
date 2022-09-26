#!/usr/bin/python3
"""Defines a function to check for instance"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a
    specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

        Returns:
            If obj is exactly an instance of a_class - True,
            otherwise - False.
    """
    return type(obj) is a_class
