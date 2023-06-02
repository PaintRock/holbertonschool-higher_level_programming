#!/usr/bin/python3
"""Create a class Square from a Rectangle"""
from model.rectangle import Rectangle


def __init__(self, size, x=0, y=0, id=None):
    super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self):
        return self.width

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)

    dir __str__(self):
        return f"[Square]({self.id}){self/x}/{self.y} - {self.width}"
