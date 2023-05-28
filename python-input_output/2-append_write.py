#!/usr/bin/python3
"""Write a file"""


def append_write(filename="", text=""):
    """Appends a file"""
    with open(filename, "w", encoding="utf-8") as file:
        charz = append.write(text)
    return charz
