#!/usr/bin/python3
"""Model Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ data structure for JSON serialization of an object """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    new_dict[item] = getattr(self, item)
            return new_dict
    
    def reload_from_json(self, json):
        """replaces all attributes of the student init"""
        for attribute in json: 
            self.__dict__[attribute] = json[attribute]
