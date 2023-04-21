#!/usr/bin/python3
"""This unit defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """displays the JSON representation of a string object"""
    return json.dumps(my_obj)
