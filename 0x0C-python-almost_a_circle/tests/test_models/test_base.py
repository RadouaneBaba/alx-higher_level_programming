#!/usr/bin/python3

""" test base class """
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ testing base class ... """
    def test_id_gen(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)
        self.assertEqual(b4.id, 3)
