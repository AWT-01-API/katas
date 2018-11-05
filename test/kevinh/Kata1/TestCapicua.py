from src.kevinh.Kata1.Capicua import Capicua
import unittest


class TestCapicua(unittest.TestCase):

    def setUp(self):
        self.capicua = Capicua()

    def test_check_true(self):
        self.assertTrue(self.capicua.checkword("oruro"))
        self.assertTrue(self.capicua.checkword("radar"))
        self.assertTrue(self.capicua.checkword("arenera"))

    def test_check_false(self):
        self.assertFalse(self.capicua.checkword("test"))
        self.assertFalse(self.capicua.checkword("desktop"))
