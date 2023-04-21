#!/usr/bin/python3
"""defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename) as f:
        return json.load(f)
