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
        """Assigns a key and value argument to each attribute """
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]

        for key, value in kwargs.items():
            """dem key values"""
            if key == "id":
                self.id = kwargs['id']
            if key == "size":
                self.height = kwargs['size']
                self.width = kwargs['size']
            if key == "x":
                self.x = kwargs['x']
            if key == "y":
                self.y = kwargs['y']
