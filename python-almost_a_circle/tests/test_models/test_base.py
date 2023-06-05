import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_init_no_id(self):
        # Test the __init__ method of Base class when no id is provided
        base = Base()
        self.assertEqual(base.id, 89)

    def test_base_init_with_id(self):
        # Test the __init__ method of Base class when an id is provided
        base = Base(42)
        self.assertEqual(base.id, 42)

if __name__ == '__main__':
    unittest.main()
