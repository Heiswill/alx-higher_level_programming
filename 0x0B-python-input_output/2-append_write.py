#!/usr/bin/python3
"""Defines append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of atext file.

    Args:
        filename (str): The Filename.
        text (str): The text to append to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
