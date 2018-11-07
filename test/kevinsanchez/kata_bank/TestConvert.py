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

    def test_read(self):
        self.convert.read()