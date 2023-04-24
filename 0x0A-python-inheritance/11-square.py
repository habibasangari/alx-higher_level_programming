#!/usr/bin/python3
"""
BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """public instance methods area and integer_validator"""
    def area(self):
        """exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation of integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle representation"""
    def __init__(self, width, height):
        """instance of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """square representation"""
    def __init__(self, size):
        """square instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"area of the square"""
        return self.__size ** 2

    def __str__(self):
        """square representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
