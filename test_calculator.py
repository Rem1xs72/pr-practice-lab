import unittest
from calculator import add


class CalculatorTests(unittest.TestCase):
    def test_integer_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_fractional_addition(self):
        self.assertAlmostEqual(add(1.25, 2.5), 3.75)

    def test_negative_addition(self):
        self.assertEqual(add(-7, 2), -5)

    def test_rejects_string_in_either_argument(self):
        for a, b in [("2", 3), (2, "3")]:
            with self.subTest(a=a, b=b), self.assertRaises(TypeError):
                add(a, b)

    def test_rejects_bool_in_either_argument(self):
        for a, b in [(True, 3), (2, False)]:
            with self.subTest(a=a, b=b), self.assertRaises(TypeError):
                add(a, b)


if __name__ == "__main__":
    unittest.main()
