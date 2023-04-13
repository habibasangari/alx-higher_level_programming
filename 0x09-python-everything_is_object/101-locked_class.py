#!/usr/bin/python3
# 101-locked_class.py

"""Defination of locked class."""


class LockedClass:
    """
    hindering the user from instantiating new LockedClass attributes
    for anything except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

