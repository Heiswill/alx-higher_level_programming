#!/usr/bin/python3
"""Defines a class MyInt that extend the `int` class"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
