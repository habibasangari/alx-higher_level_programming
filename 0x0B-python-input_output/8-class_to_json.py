#!/usr/bin/python3
"""The unit defines a Python class-to-JSON function"""


def class_to_json(obj):
    """displays dictionary representation of a simple data structure"""
    return obj.__dict__
