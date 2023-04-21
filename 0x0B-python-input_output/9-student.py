#!/usr/bin/python3
""definition of a class Student"""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """starts new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """displays the  dictionary representation of the Student"""
        return self.__dict__
