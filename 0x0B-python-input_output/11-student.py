#!/usr/bin/python3
"""The unit defines a class Student"""


class Student:
    """Representation a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the Student.
        attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """changes all attributes of the Student
        """
        for x, v in json.items():
            setattr(self, x, y)
