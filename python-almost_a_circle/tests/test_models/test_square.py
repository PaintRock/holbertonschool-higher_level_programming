#!/usr/bin/python3
"""
This is the unittest module for the square class
"""


import unittest
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class test_square(unittest.TestCase):
    """
    This class will unittest the Sectangle class
    """

    def test_module_docstring(self):
        """
        Test rectangle module documentation exists
        """
        self.assertTrue(len(__import__('models').square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Rectangle class documentation exists
        """
        self.assertTrue(len(__import__('models').square.Square.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests Rectangle methods for documentation
        """
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)

    def test_pep8_compliance(self):
        """
        Tests to ensure models/rectangle and
        /tests/test_models/rectangle_base.py are pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_build_a_square(self):
        """
        Tests that a square is built correctly
        """
        square1 = Square(2, 4, 6, 8)
        self.assertEqual(square1.size, 2)
        self.assertEqual(square1.x, 4)
        self.assertEqual(square1.y, 6)
        self.assertEqual(square1.id, 8)
        square2 = Square(3, 0, 0, -8)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 0)
        self.assertEqual(square2.y, 0)
        self.assertEqual(square2.id, -8)
        square3 = Square(1)
        self.assertEqual(square3.size, 1)
        square4 = Square(1, 2)
        self.assertEqual(square4.size, 1)
        self.assertEqual(square4.x, 2)
        square5 = Square(1, 2, 3)
        self.assertEqual(square5.size, 1)
        self.assertEqual(square5.x, 2)
        self.assertEqual(square5.y, 3)

    def test_build_a_bad_square(self):
        """
        Multiple tests for value and type errors in square
        """
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            Square("size", 2, 3, 4)
        with self.assertRaises(TypeError):
            Square(1, "x", 3, 4)
        with self.assertRaises(TypeError):
            Square(1, 2, "y", 4)
        with self.assertRaises(ValueError):
            Square(-4, 2, 3, 4)
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 4)
        with self.assertRaises(ValueError):
            Square(1, -2, 0, 4)
        with self.assertRaises(ValueError):
            Square(1, 2, -3, 4)

    def test_area(self):
        """
        Testing area function for square
        """
        square1 = Square(4, 1, 1, 1)
        self.assertEqual(square1.area(), 16)
        square2 = Square(1, 1, 1, 1)
        self.assertEqual(square2.area(), 1)

    def test_display(self):
        """
        Testing proper function of display method
        """
        square1 = Square(3, 0, 0, 1)
        square2 = Square(2, 2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as out:
            square1.display()
            self.assertEqual('###\n###\n###\n', out.getvalue())
        with patch('sys.stdout', new=StringIO()) as out:
            square2.display()
            self.assertEqual('\n\n  ##\n  ##\n', out.getvalue())

    def test___str__(self):
        """
        Tests for proper use of __str__ method
        """
        square1 = Square(6, 2, 4, 69)
        self.assertEqual(square1.__str__(), "[Square] (69) 2/4 - 6")

    def test_update(self):
        """
        Tests for proper use of update method
        """
        square1 = Square(2, 3, 4, 1)
        square2 = Square(2, 3, 4, 5)
        self.assertNotEqual(str(square1), str(square2))
        square2.update(id=1)
        self.assertEqual(str(square1), str(square2))
        s3 = Square(3, 6, 9, 0)
        s4 = Square(1, 2, 3, 4)
        s4.update(0, 3, 6, 9)
        self.assertEqual(str(s3), str(s4))

    def test_to_dictionary(self):
        """
        Tests for proper use of to_dictionary method
        """
        s1 = Square(10, 2, 1, 0)
        s1_dictionary = s1.to_dictionary()
        self.assertTrue(type(s1_dictionary) is dict)
        self.assertTrue(type(s1) is Square)

if __name__ == '__main__':
    unittest.main()
