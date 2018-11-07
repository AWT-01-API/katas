import unittest
from src.kevinsanchez.kata_bank.Store import Store
from src.kevinsanchez.kata_bank.Convert import Convert
"""
test class.
"""
class TestStore(unittest.TestCase):

    """
    setup.
    """
    def setUp(self):
        self.convert = Convert()
    """
    test for read.
    """
    def test_read(self):
        Store.store_data(self.convert.extract())
