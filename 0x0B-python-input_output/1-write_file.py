#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file and return
    the number of characters written.

    Args:
        filename (str): Filename.
        text (str): Text to write to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
