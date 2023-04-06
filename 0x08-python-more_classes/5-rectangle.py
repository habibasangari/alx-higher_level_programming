#!/usr/bin/python3
"""
defination of class Rectangle
"""


class Rectangle:
    """represents rectangle"""
    def __init__(self, width=0, height=0):
        """initialization of rectangle"""
        self.width = width
        self.height = height

    def __del__(self):
        """shows a string if an instance is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """shows string representation of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for x in range(self.__height))
        return string

    def __repr__(self):
        """string representation of rectangle in production"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
