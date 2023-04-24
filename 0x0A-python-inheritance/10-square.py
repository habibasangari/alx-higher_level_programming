#!/usr/bin/python3
"""
holds class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square representation"""
    def __init__(self, size):
        """instance of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"area of the square"""
        return self.__size ** 2
