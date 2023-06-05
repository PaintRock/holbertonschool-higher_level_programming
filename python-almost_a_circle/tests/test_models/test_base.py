#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset __nb_objects counter. print test"""
        print("Base setUp")
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

    def test_constructor_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj1 = Base(1)
        obj2 = Base(2)
        obj3 = Base(3)
        data = [obj1.to_dictionary(), obj2.to_dictionary(), obj3.to_dictionary()]
        json_string = Base.to_json_string(data)
        expected_result = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        self.assertEqual(json_string, expected_result)

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        obj3 = Base(3)
        Base.save_to_file([obj1, obj2, obj3])
        # Perform assertions to check if the file was saved correctly

    def test_create_rectangle(self):
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5}
        obj = Base.create(**rectangle_dict)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 5)

    def test_create_square(self):
        square_dict = {'id': 1, 'size': 5}
        obj = Base.create(**square_dict)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 5)

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[2]['id'], 3)

    def test_load_from_file(self):
        test_file = 'test_data.json'
        test_data = [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
        # Save test data to a file
        Base.save_to_file(test_data, test_file)

        # Load objects from the file
        loaded_data = Base.load_from_file(test_file)

        # Assert the loaded data is correct
        self.assertEqual(len(loaded_data), 3)
        self.assertEqual(loaded_data[0]['id'], 1)
        self.assertEqual(loaded_data[1]['id'], 2)
        self.assertEqual(loaded_data[2]['id'], 3)

        # Cleanup: Remove the test file
        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
