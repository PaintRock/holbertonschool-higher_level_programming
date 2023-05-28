#!/usr/bin/python3
"""Write a file"""


def append_write(filename="", text=""):
    """Appends a file"""
    with open(filename, "a", encoding="utf-8") as file:
        charz = file.write(text)
    return charz
