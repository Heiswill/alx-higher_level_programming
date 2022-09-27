#!/usr/bin/python3
"""Defines the load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Function that creates an Oject from a "JSON file".

    Args:
        filename (str): Name of file.
    """
    with open(filename, "r") as f:
        return json.load(f)
