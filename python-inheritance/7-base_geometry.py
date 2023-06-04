#!/usr/bin/python3
"""Write a class BaseGeometry with a public instance method 'def area(self)'
that raises an Exception with a message.  And another public instance method
'def integer_validator"""


class BaseGeometry:
    """Public instance method def area(self) """
    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method def integer_validator"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
