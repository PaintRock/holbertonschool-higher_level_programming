#!/usr/bin/python3
"""Student class to a dictionary"""


class Student:
    """This method initializes the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method return a json representation of a class"""
        return self.__dict__
