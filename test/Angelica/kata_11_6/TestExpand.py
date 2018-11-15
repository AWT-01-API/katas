import unittest
from src.Angelica.kata_11_6.expand import expanded_form

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        num = expanded_form(42)
        self.assertItemsEqual(num,'40 + 2')