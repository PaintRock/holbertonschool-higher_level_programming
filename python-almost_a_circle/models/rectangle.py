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
        if type value is not (int):
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
        if type value is not (int):
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
        if type value is not (int):
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
        if type value is not (int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

# Public instance methods
    def area(self):
        """ Public instance method that returns the area of the Rectangle.
            Returns:
                The area of the Rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Public instance method that prints
        the Rectangle instance with '#' character in stdout.
        ''Updated:'' to handle x and y offsets.
        Returns: The area of the Rectangle. """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """ Public instance that returns the dictionary representation
        of a Rectangle.
        Returns:
            A dictionary representation of a Rectangle. """
        return {
            "id":  self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Public instance method that assigns an argument to each attribute.
        Args:
            *args (list): A list of arguments.
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            ''updated'': to assign key/value argument to attributes.
            **kwargs (dict): A dictionary of key/value
            arguments to assign to attributes.
                **kwargs are skipped if *args exist and is
                not empty
            Each key in the dictionary represents an attribute to the instance.
            **order was super important for args to work
        but with kwargs order is not important.**
        Returns: None
                """
        attributes = ["id", 'width', "height", 'x', "y"]
        #  if args exist and is not empty, use args
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        # if no args exist or args id empty use kwargs
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Public instance method that returns a string representation of
        the Rectangle instance.
        Return:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            ))
