#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test cases for a max_integer function """
    def test_max(self):
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertAlmostEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertAlmostEqual(max_integer([1, -4, 4.2, 1, 6, 7.3]), 7.3)
