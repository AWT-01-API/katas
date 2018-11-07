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
    test for extract method.
    """
    def test_extract(self):
        list_file_rows = ["123456789",
                          "000000000",
                          "111111111",
                          "222222222",
                          "333333333",
                          "888888888"]
        position = 0
        for value in self.convert.extract():
            self.assertEqual(list_file_rows[position], value)
            position += 1