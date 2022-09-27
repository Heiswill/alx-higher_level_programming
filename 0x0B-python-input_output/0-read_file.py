#!/usr/bin/python3
"""Defines a read_file function"""


def read_file(filename=""):
    """Reads a file and prints to stdout
    Args:
        filename (str): Filename.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
