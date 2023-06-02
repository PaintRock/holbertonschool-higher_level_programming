#!/usr/bin/python3
"""Create a class Square from a Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize the class Square that uses the data from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"