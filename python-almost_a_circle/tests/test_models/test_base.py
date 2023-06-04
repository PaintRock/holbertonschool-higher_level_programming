import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        '''test the automatic assignment of incremental ids, and the
        assignment of specific id when provided'''
        base1 = Base()
        base2 = Base()
        base3 = Base(100)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 100)

    def test_id_type(self):
        '''test the type of id attribute to ensure an integer'''
        base = Base(10)
        self.assertIsInstance(base.id, int)

if __name__ == '__main__':
    unittest.main()
