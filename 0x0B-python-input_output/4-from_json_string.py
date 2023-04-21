#!/usr/bin/python3
"""This unit defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """displays the Python object representation of a JSON string"""
    return json.loads(my_str)
