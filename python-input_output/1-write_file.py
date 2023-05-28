#!/usr/bin/python3
"""read a file"""


def read_file(filename=""):
    """Opens and reads a specific file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
