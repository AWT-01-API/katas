import unittest
from src.Angelica.kata_11_6.reverse import reverse_alternate

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        text = reverse_alternate("Did it work?")
        self.assertItemsEqual(text,"Did ti work?")


