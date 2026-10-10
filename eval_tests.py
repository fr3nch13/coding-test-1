import unittest
from eval import eval_sanitize

class TestMathFunctions(unittest.TestCase):

    def test_sanitize_valid_string(self):
        self.assertEqual(eval_sanitize(" 4 + 4 "), "4+4")
        self.assertEqual(eval_sanitize("6 +3-2"), "6+3-2")
        self.assertEqual(eval_sanitize("5 * 6 + ((202/2) - 1)"), "5*6+((202/2)-1)")

    def test_sanitize_invalid_character(self):
        with self.assertRaises(ValueError):
            eval_sanitize("3 + a")

    def test_sanitize_empty_string(self):
        self.assertEqual(eval_sanitize(" "), "")

if __name__ == '__main__':
    unittest.main()