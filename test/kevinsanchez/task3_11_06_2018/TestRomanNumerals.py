import unittest
from src.kevinsanchez.task3_11_06_2018.RomanNumerals import RomanNumerals

"""
test class.
"""
class TestRomanNumerals(unittest.TestCase):

    """
    setUp for test class.
    """
    def setUp(self):
        self.roman = RomanNumerals()

    """
    test method to roman conversion.
    """
    def test_to_roman(self):
        self.assertEqual("I", self.roman.to_roman(1))
        self.assertEqual("M", self.roman.to_roman(1000))
        self.assertEqual("CMXCIX", self.roman.to_roman(999))
        self.assertEqual("IV", self.roman.to_roman(4))
        self.assertEqual("MCMXCI", self.roman.to_roman(1991))
        self.assertEqual("MMVI", self.roman.to_roman(2006))
        self.assertEqual("MMXX", self.roman.to_roman(2020))

    """
    test method from roman conversion.
    """
    def test_from_roman(self):
        self.assertEqual(self.roman.from_roman('XXI'), 21)
        self.assertEqual(self.roman.from_roman('I'), 1)
        self.assertEqual(self.roman.from_roman('III'), 3)
        self.assertEqual(self.roman.from_roman('IV'), 4)
        self.assertEqual(self.roman.from_roman('MMVII'), 2007)
        self.assertEqual(self.roman.from_roman('MDCLXIX'), 1669)
