#!/usr/bin/python3
"""this documentation is for Crystal"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestSqure(unittest.TestCase):
"""Why no one knows"""
    
     def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Square setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Base._Base__nb_objects = 0

        self.base = Base()

    def tearDown(self):
        print("Base tearDown")

        sys.stdout = sys.__stdout__

        del self.base
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass
            
    def test_Square_constructor(self):
        s = Square(1, )
        """does a square exist?"""
        self.assertIsNotNone(s)
        # Additional test for specific dimensions
        self.assertEqual(s.width, 1)
