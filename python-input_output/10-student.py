#!/usr/bin/python3
"""Write a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Init class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""
        if attrs is None:
            return self.__dict__
        else:
            make_new = {}
            for item in attrs:
                if hasattr(self, item):
                    make_new[item] gitattr(self, item)
        return make_new
