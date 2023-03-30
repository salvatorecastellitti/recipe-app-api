"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test calc module
    """

    def test_add_numbers(self):
        """test add number tigheter"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """test subtract numbers"""
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
