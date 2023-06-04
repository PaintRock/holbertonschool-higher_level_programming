#!/usr/bin/python3


""" Write the class Rectangle that inherits from Base."""


# Import the Base class
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base class.    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of the Rectangle class. Inherits from Base class. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Getters and Setters
    @property
    def width(self):
        """ Getter for the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the __width of the Rectangle"""
        if type(value) is not (int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height of the Rectangle """
        if type(value) is not (int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the private instance attribute: 'x' of the Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x of the Rectangle. """
        if type(value) is not (int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the private instance attribute y of the Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the private instance attribute y """
        if type(value) is not (int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

# Public instance methods
    def area(self):
        """ Public instance method for th area of the Rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Public instance method that prints
        the Rectangle instance with '#' character in stdout.
        The area of the Rectangle. """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """ Public instance that returns the dictionary representation"""
        return {
            "id":  self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        if args:  # Check if *args exists and is not empty
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']

    def __str__(self):
        """ Public instance method that returns a string representation of
        the Rectangle instance."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            ))
