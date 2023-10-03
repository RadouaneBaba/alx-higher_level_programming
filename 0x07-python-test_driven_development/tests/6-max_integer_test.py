#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer
""" test module """


class TestMaxInteger(unittest.TestCase):
    """ class to test max_integer function """
    def test_max(self):
        self.assertEqual(max_integer([1, 4, 3, 5, -2, 0]), 5)
        self.assertEqual(max_integer([-1, 0, -2, -3]), 0)
        self.assertEqual(max_integer([-7, -4, -3, -5, -2]), -2)
        self.assertEqual(max_integer([]), None)
