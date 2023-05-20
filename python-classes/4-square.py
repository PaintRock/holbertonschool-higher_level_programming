#!/usr/bin/python3
"""
Defines an empty class Square with size attribute
"""


class Square:
    """ Defines Square class with private size attribute """
    def __init__(self, size=0):
        self.__size = size

        """property"""
        def size(self):
            return self.__size

        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
