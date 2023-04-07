#!/usr/bin/python3
"""
"3-say_my-name" module
3-say_my_name module provides a function, say_my_name
"""


def say_my_name(first_name, last_name=""):
    """display "my name is" follow by first name, optionally last name"""
    if type(first_name) is not str:
        raise TypeError("the first_name should be string")
    if type(last_name) is not str:
        raise TypeError(" the last_name should be string")
    print("My name is", first_name, last_name)
