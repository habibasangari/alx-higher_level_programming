#!/usr/bin/python3
"""
this contains the MyList class
"""


class MyList(list):
    """this is a subclass of list"""
    def __init__(self):
        """ shows the initialization of the object"""
        super().__init__()

    def print_sorted(self):
        """this prints the sorted list in ascending order"""
        print(sorted(self))

