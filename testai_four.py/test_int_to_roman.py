# pylint: disable= missing-docstring
import unittest
from task_four import int_to_roman


class TestRoman(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual("V", int_to_roman(5))
        # self.assertEqual(20.5456936226167, kmi(50, 1.56))
        # self.assertEqual(27.70083102493075, kmi(100, 1.90))
