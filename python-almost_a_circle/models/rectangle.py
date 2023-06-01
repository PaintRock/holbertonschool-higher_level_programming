#!/usr/bin/python3
from models.base import Base
"""Write a class Rectangle that inherits from Base"""


class Rectangle(Base):
    """Create a child of Base called Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """def all that is in the rectangle"""
        super().__init__(id)
