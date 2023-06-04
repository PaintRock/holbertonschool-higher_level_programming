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

    def update(self, *args, **kwargs):
        """ Update the class Square by adding the public method
        def update(self, *args, **kwargs) that assigns attributes:
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance"""
        attributes = ["id", 'width', "height", 'x', "y"]

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
