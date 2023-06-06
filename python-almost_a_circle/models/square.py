#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create a child class of Rectangle called Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes of the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides the string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

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
        """ Public instance method that assigns an argument to each
        attribute."""

        attributes = ["id", 'width', "height", 'x', "y"]
        #  if args exist and is not empty, use args
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        # if no args exist or args id empty use kwargs
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
