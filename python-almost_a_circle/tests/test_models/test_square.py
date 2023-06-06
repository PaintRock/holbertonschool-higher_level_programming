#!/usr/bin/python3
""" This module is a unittest for the Base class """

"""import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """ test class for Base class """
    # setup and teardown methods are called before and after each test
    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Base._Base__nb_objects = 0

        self.base = Base()

    def tearDown(self):
        print("Base tearDown")"""

        sys.stdout = sys.__stdout__

        del self.base
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass
