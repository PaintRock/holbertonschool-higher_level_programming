#!/bin/usr/python3
"""program that prints a square"""


#!/usr/bin/python3
"""Class attribute"""


def print_square(size):
    """prints a square, maybe"""

    """checks for integer and positive value"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
