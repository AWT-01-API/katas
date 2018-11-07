import unittest
from src.kevinsanchez.kata_bank.Checksum import Checksum


class ChecksumTest(unittest.TestCase):

    """
    Setup accounts.
    """
    def setUp(self):
        self.invalid_account = "123456789"
        self.valid_account = "020000001"

    def test_checksum_true(self):
        self.assertEqual(Checksum.calculate(self.valid_account), True)

    def test_checksum_false(self):
        self.assertEqual(Checksum.calculate(self.invalid_account), False)
