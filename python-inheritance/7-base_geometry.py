#!/usr/bin/python3
"""Write a class BaseGeometry with a public instance method 'def area(self)'
that raises an Exception with a message.  And another public instance method
'def integer_validator"""


class BaseGeometry:
    """Public instance method 'def area(self)' """
    def area(self):
        raise Exception("area{} is not implemented")

    """Public instance method 'def integer_validator'"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
