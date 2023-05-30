#!/usr/bin/python3
"""Returns True if the object is an instance that inherited
directly or indirectly from the specified class"""


def inherits_from(obj, a_class):
    """checks to see if the subclass is a part of the superclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
