#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """check if the variables are strings"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name is None:
        first_name == ""

    if last_name is None:
        last_name == ""

    print("My name is {}{}".format(first_name, last_name))
