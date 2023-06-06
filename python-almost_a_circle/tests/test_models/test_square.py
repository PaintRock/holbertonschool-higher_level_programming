#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestSqure(unittest.TestCase):


    def test_Square_constructor(self):
        s = Square(1, )
        """does a square exist?"""
        self.assertIsNotNone(s)
        # Additional test for specific dimensions
        self.assertEqual(s.width, 1)
