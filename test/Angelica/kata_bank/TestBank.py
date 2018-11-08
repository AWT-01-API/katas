import unittest
from src.Angelica.kata_bank.Convertor import Convertor

class ConvertTest(unittest.TestCase):

    def test_validate_all_codes(self):
        convert = Convertor("source_data.txt")
        codes = convert.get_all_codes()
        self.assertTrue(convert.validate_all_codes(codes))
