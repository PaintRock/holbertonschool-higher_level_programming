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
