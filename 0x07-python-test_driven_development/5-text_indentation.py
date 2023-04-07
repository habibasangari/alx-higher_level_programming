#!/usr/bin/python3
"""
"5-text_indentation" module
5-text_indentation module provides a function, text_indentation(text)
"""


def text_indentation(text):
    """divides text into lines along "?", ":", "." follow by two lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for x in text:
        if flag == 0:
            if x == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if x == '?' or x == '.' or x == ':':
                print(x)
                print()
                flag = 0
            else:
                print(x, end="")

