#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """This opens and reads a specific file 'utf-8'"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

    
