from src.Angelica.kata_bank.Converter import Converter
import unittest


class ConvertTest(unittest.TestCase):

    def setUp(self):
        self.convert = Converter("source_data.txt")

    def test_all_text_codes_conversion(self):
        codes = self.convert.get_all_codes()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], codes[0])
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], codes[1])
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1, 1], codes[2])
        self.assertEqual([2, 2, 2, 2, 2, 2, 2, 2, 2], codes[3])
        self.assertEqual([3, 3, 3, 3, 3, 3, 3, 3, 3], codes[4])
        self.assertEqual([8, 8, 8, 8, 8, 8, 8, 8, 8], codes[5])

    def test_matrix0_to_number(self):
        matrix0 = [[' ', '_', ' '],
                   ['|', ' ', '|'],
                   ['|', '_', '|']]
        self.assertEqual(0, self.convert.get_dict_key_by_value(matrix0))

    def test_textcode_to_matrix(self):
        text_to_convert = [" _  _  _  _  _  _  _  _  _ ",
                           "| || || || || || || || || |",
                           "|_||_||_||_||_||_||_||_||_|"]
        matrix0 = [[' ', '_', ' '],
                   ['|', ' ', '|'],
                   ['|', '_', '|']]
        expected_matrix = [matrix0, matrix0, matrix0, matrix0, matrix0, matrix0, matrix0, matrix0, matrix0]
        self.assertEqual(expected_matrix, self.convert.get_code_matrix_list(text_to_convert))
