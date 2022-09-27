#!/usr/bin/python3
import json
"""Defines a to_json_string function"""


def to_json_string(my_obj):
    """Function that returns the JSON representation
    of an object(string)

    Args:
        my_obj (str): String object.
    """
    return json.dumps(my_obj)
