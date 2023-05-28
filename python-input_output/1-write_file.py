#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename,"w" , encoding="utf-8") as file:
        charz = file.write(text)
    return charz
