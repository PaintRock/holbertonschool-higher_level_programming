#!/usr/bin/python3
"""Method that contain the Base-Geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method return the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """This method return the string of the rectagle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
