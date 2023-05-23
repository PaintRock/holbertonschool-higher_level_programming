#!/usr/bin/python3
"""create an empty class called Rectangle"""


"""create the class Rectangle"""


class Rectangle:

    """include class because it cannot be empty"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.width * 2 + self.__height * 2

    """ prints rectangle with # """
    def __str__(self):
        tangleO = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    tangleO.append("#")
                if i < self.__height - 1:
                    tangleO.append("\n")
        tangleO = "".join(tangleO)
        return tangleO

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
