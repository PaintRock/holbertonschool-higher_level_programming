#!/usr/bin/python3
"""Write a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create a child class of Base called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate the attributes of the Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self, value):
        """ Getter for width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width and raise errors if incorrect value is entered"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height and raise errors if incorrect value is entered"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x and raise errors if incorrect value is entered """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y and raise errors if incorrect value is entered """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area (width times height)"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using # and the kiss method"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Overrides the string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.__x, self.__y, self.__width, self.__height)
