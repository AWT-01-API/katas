import unittest
from src.kevinsanchez.kata_bank.Convert import Convert
"""
test class.
"""
class TestConvert(unittest.TestCase):

    """
    setpup.
    """
    def setUp(self):
        self.convert = Convert()
    """
    test for read.
    """
    def test_read(self):
        print(self.convert.extract())
