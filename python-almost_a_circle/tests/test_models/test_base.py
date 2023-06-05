#!/usr/bin/python3
import unittest
import io
import sys
import os
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset __nb_objects counter. print test"""
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

        Base._Base__nb_objects = 0

    def tearDown(self):
        sys.stdout = sys.__stdout__
        print("Base tearDown")

        del Base._Base__nb_objects
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_constructor_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        """ Test to_json_string method:
        returns the JSON string representation of list_directories
        """
        # test empty list
        self.assertEqual(Base.to_json_string([]), "[]")
        # test None
        self.assertEqual(Base.to_json_string(None), "[]")
        # test normal list
        list_directories = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
            ]
        expected_json = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        self.assertEqual(Base.to_json_string(list_directories), expected_json)
   
    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[2]['id'], 3)

if __name__ == '__main__':
    unittest.main()
