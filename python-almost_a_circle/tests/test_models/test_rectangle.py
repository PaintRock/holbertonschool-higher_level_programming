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
            'idth': 2,
            'h

    def test_rectangle_constructor(self):
        r = Rectangle(1, 2)
        self.assertIsNotNone(r)

    def test_rectangle_getters_and_setters(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

        r.width = 3
        r.height = 4
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_rectangle_invalid_width_and_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {
            "id": 5,
            "width": 1,
            "height": 2,
            "x": 3,
            "y": 4
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

    def test_rectangle_update(self):
        r = Rectangle(1, 2)
        r.update(3, 4, 5, 6, 7)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

        r.update(id=8, width=9, height=10, x=11, y=12)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)
        self.assertEqual(r.y, 12)
        self.assertEqual(r.id, 8)

    def test_rectangle_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_str = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()