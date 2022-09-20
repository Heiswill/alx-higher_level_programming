#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """Prevent user from dynamically creating new instance
        attributes, except the new instance attribute is
        called first_name.
    """
    __slots__ = ["first_name"]

    def __init__(self):
        pass
