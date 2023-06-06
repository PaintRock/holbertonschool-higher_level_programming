#!/usr/bin/python3
""" This module is a unittest for the Rectangle class """

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle class """
    def setUp(self):
        """Set up test method"""
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.rectangle = Rectangle(1, 1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0
        # print(f"Base.__nb_objects after reset: {Base._Base__nb_objects}")

    def tearDown(self):
        """Tear down test method"""
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_rectangle_constructor(self):
        r = Rectangle(1, 2)
        self.assertIsNotNone(r)
        # Additional test for specific dimensions
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    # test id assignment and if it increments correctly
    def test_id(self):
        """Test __init__ method:
        id assignment in the Rectangle class.
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)

    def test_area(self):
        # Create a rectangle with width=3 and height=4
        rectangle = Rectangle(3, 4)
        # Check if the area is calculated correctly
        self.assertEqual(rectangle.area(), 12)

    def test_display(self):
        # Create a rectangle with width=5 and height=3
        rectangle = Rectangle(5, 3)
        # Display the rectangle
        rectangle.display()
        # No assertion is made here, it's just for visual inspection

    def test_to_dictionary(self):
        # Create a rectangle with width=2, height=6, x=1, y=2, and id=42
        rectangle = Rectangle(2, 6, 1, 2, 42)
        # Convert the rectangle to a dictionary
        dictionary = rectangle.to_dictionary()
        # Check if the dictionary contains the expected values
        self.assertEqual(dictionary, {
            'id': 42,
            'width': 2,
            'height': 6,
            'x': 1,
            'y': 2
        })

    def test_update(self):
        # Create a rectangle with width=2, height=3, x=1, y=1, and id=1
        rectangle = Rectangle(2, 3, 1, 1, 1)
        # Update the rectangle with new values
        rectangle.update(5, 4, 3, 2, 1)
        # Check if the attributes have been updated correctly
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 5)

    def test_str(self):
        # Create a rectangle with width=3, height=4, x=1, y=2, and id=42
        rectangle = Rectangle(3, 4, 1, 2, 42)
        # Check if the string representation is correct
        self.assertEqual(str(rectangle), "[Rectangle] (42) 1/2 - 3/4")


if __name__ == '__main__':
    unittest.main()
