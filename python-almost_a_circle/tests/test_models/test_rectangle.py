#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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
