import unittest

from no_eval import calculate, sanitize

class TestCalculate(unittest.TestCase):

    def test_sanitize_valid_string(self):
        self.assertEqual(sanitize(" 4 + 4 "), "4+4")
        self.assertEqual(sanitize("6 +3-2"), "6+3-2")
        self.assertEqual(sanitize("5 * 6 + ((202/2) - 1)"), "5*6+((202/2)-1)")

    def test_examples(self):
        for expression, expected in [
            ("4 + 4", eval("4 + 4")),
            ("6 +3-2", eval("6 +3-2")),
            ("5 * 6 + (202/2)", eval("5 * 6 + (202/2)")),
        ]:
            with self.subTest(expression=expression):
                self.assertEqual(calculate(expression), expected)

if __name__ == '__main__':
    unittest.main()