# pylint: disable= missing-docstring

import unittest
from main import is_leap


class TestLeap(unittest.TestCase):
    def test_is_leap(self):
        result = is_leap(2000)
        self.assertTrue(result)

    def test_not_leap(self):
        result = is_leap(2100)
        self.assertFalse(result)


# python3 -m unittest test_keliamieji.py
# if __name__ == "__main__":
#     unittest.main()
