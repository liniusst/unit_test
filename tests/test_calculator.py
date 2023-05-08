# pylint: disable= missing-docstring

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(a=2, b=2), 4)
        self.assertEqual(calculator.add(a=-2, b=2), 0)
        self.assertEqual(calculator.add(a=10, b=100), 110)

    def test_sub(self):
        self.assertEqual(calculator.sub(a=2, b=2), 0)
        self.assertEqual(calculator.sub(a=-2, b=2), -4)
        self.assertEqual(calculator.sub(a=10, b=100), -90)

    def test_mult(self):
        self.assertEqual(calculator.mult(a=2, b=2), 4)
        self.assertEqual(calculator.mult(a=5, b=2), 10)
        self.assertEqual(calculator.mult(a=10, b=100), 1000)

    def test_div(self):
        self.assertEqual(calculator.div(a=6, b=2), 3)
        self.assertEqual(calculator.div(a=50, b=2), 25)
        self.assertEqual(calculator.div(a=22, b=2), 11)
        self.assertRaises(ZeroDivisionError, calculator.div, 1, 0)
