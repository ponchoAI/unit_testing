# test_calculator.py

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(5, 3), 8)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(-1, 1), -2)
        self.assertEqual(Calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(5, 3), 15)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(-6, 3), -2)
        self.assertEqual(Calculator.divide(6, -3), -2)
        self.assertEqual(Calculator.divide(-6, -3), 2)

        # Test division by zero
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
