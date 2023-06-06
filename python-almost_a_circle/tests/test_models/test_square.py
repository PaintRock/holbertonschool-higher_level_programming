#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base


"""Circle tests"""


    def test_Square_constructor(self):
        s = Square(1, 2)
        self.assertIsNotNone(s)
        # Additional test for specific dimensions
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 2)
