#!/usr/bin/python3
"""
BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """public instance methods area and integer_validator"""
    def area(self):
        """displays exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation of integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """a rectangle representation"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
