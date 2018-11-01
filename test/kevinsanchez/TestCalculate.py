import unittest
from src.kevinsanchez.Calculate import Calculate

"""
Test for class calculate.
"""
class TestCalculate(unittest.TestCase):

    """
    creation of the instance.
    """
    def setUp(self):
        self.calculate = Calculate()

    """
    test factorial method.
    """
    def test_fact(self):
        self.assertEqual(self.calculate.fact(3), 6)
        self.assertEqual(self.calculate.fact(1), 1)
        self.assertEqual(self.calculate.fact(2), 2)

    """
    test is capicua method
    """
    def test_is_capicua(self):
        self.assertTrue(self.calculate.is_capicua("oruro"))
        self.assertFalse(self.calculate.is_capicua("orur"))
        self.assertTrue(self.calculate.is_capicua("121"))
        self.assertTrue(self.calculate.is_capicua("1"))
