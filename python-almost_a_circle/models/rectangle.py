#!/usr/bin/python3
"""Write a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create a child class of Base called Rectangle"""

    class Rectangle(Base):
        """Rectangle class initialization"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    """width getter"""
    def get_width(self):
        return self.__width
    
    @property
    """height getter"""
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y
    
    @width.setter
    def set_width(self, value):
        self.__width = width

    @x.setter
    def set_x(self, value):
        self.__x = x

    @height.setter
    def set_height(self, value):
        self.__height = height

    @y.setter
    def set_y(self, value):
        self.__y = y
