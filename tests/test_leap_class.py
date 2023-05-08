# pylint: disable= missing-docstring

import unittest
from leap import Leap


class TestLeap(unittest.TestCase):
    def setUp(self) -> None:
        self.leap = Leap()

    def test_check_method(self):
        self.assertTrue(self.leap.leap_check(2000))
        self.assertTrue(self.leap.leap_check(2020))

    def test_range_method(self):
        result = self.leap.leap_range(1980, 2000)
        self.assertEqual(result, [1980, 1984, 1988, 1992, 1996])
