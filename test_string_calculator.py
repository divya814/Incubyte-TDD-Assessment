import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_single_number(self):
        self.assertEqual(StringCalculator().add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(StringCalculator().add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator().add("1,2,3,4,15"), 25)
        self.assertEqual(StringCalculator().add("10,20,30"), 60)

    def test_newline_delimiter(self):
        self.assertEqual(StringCalculator().add("1\n2,3"), 6)
        self.assertEqual(StringCalculator().add("1\n2\n3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(StringCalculator().add("//;\n1;2"), 3)  # Custom delimiter ";"
        self.assertEqual(StringCalculator().add("//-\n5-7-2"), 14)  # Custom delimiter "-"
        self.assertEqual(StringCalculator().add("//|\n2|3|4"), 9)  # Custom delimiter "|"

    # New tests for multi-character delimiters
    def test_long_delimiter(self):
        self.assertEqual(StringCalculator().add("//[***]\n1***2***3"), 6)  # Multi-char delimiter
        self.assertEqual(StringCalculator().add("//[**]\n4**5**6"), 15)  # Multi-char delimiter
        self.assertEqual(StringCalculator().add("//[%%]\n10%%20%%30%%40"), 100)  # Multi-char delimiter

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator().add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")

        with self.assertRaises(ValueError) as context:
            StringCalculator().add("-1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1, -2")

    # Test for ignoring large numbers
    def test_ignore_large_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("2,1001"), 2)  # Should ignore 1001
        self.assertEqual(calc.add("1000,1001,1002,5"), 1005)  # Only 1000 and 5 should be summed

    def test_get_called_count(self):
        calc = StringCalculator()
        calc.add("1,2,3")
        calc.add("4,5")
        self.assertEqual(calc.get_called_count(), 2)  # Expect 2 calls to add()

if __name__ == '__main__':
    unittest.main()
