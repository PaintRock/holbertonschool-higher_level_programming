#!/usr/bin/python3
""" This module is a unittest for the Base class """

import unittest
import os
import io
import sys
from models.square import Square


class TestSquare(unittest.TestCase):
    """ test class for Base class """
    # setup and teardown methods are called before and after each test
    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Square setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Square._Square__nb_objects = 0

        self.square = Square()

    def tearDown(self):
        print("Square tearDown")

        sys.stdout = sys.__stdout__

        del self.square
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
