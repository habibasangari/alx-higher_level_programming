#!/usr/bin/python3
"""unit of the class Student"""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the Student
        attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
