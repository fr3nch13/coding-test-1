import unittest
from main import sanitize

class TestMathFunctions(unittest.TestCase):

    def test_sanitize_valid_string(self):
        self.assertEqual(sanitize(" 4 + 4 "), "4+4")
        self.assertEqual(sanitize("6 +3-2"), "6+3-2")
        self.assertEqual(sanitize("5 * 6 + ((202/2) - 1)"), "5*6+((202/2)-1)")

    def test_sanitize_invalid_character(self):
        with self.assertRaises(ValueError):
            sanitize("3 + a")

    def test_sanitize_empty_string(self):
        self.assertEqual(sanitize(" "), "")