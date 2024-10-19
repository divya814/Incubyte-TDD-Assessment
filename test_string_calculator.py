import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4,15"), 25)  # Test for any number of inputs
        self.assertEqual(add("10,20,30"), 60)
        self.assertEqual(add("140,320,370,1012"),1842)

if __name__ == '__main__':
    unittest.main()
