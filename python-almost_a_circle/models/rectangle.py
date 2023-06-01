#!/usr/bin/python3
"""Write a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create a child of Base called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """def all that is in the rectangle"""
        super().__init__(id)
        self.__width == width
        self.__height == height
        self.__x = x
        self.__y = y

    
    @property
    def get_width(self):
        return.self__width

    @property
    def set_width(self):
        self.__width = width

    @property
    def get_height(self):
        return.self__height

    @property
    def set_height(self):
        self.__height = height

    @property
    def get_x(self):
        return.self__x

    @property
    def set_x(self):
        self.__x = x

    @property
    def get_y(self):
        self.__y = y
