"""Trying sample tests"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Testing the calc module"""

    def test_add_num(self):
        """test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_num(self):
        """test subtracting numbers together"""
        res = calc.subtract(15, 5)

        self.assertEqual(res, 10)
