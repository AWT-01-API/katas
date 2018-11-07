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
    test for write a new file.
    """
    def test_write(self):
        Store.store_data(self.convert.extract())
