#!/usr/bin/python3
"""Student Class"""


class Student:
    """Initializes the attributes of the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to json(self):
        """Public method to retrieve a dictionary rep of Student"""
        return self.__dict__
