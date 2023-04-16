#!/usr/bin/python3
"""
this contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """requite true if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
