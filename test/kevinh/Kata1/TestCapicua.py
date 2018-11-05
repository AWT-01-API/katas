from src.kevinh.Kata1.Capicua import Capicua
import unittest


class TestCapicua(unittest.TestCase):

    def test_check_true(self):
        capicua = Capicua()
        self.assertTrue(capicua.checkWord("oruro"))
        self.assertTrue(capicua.checkWord("radar"))
        self.assertTrue(capicua.checkWord("arenera"))

    def test_check_false(self):
        capicua = Capicua()
        self.assertFalse(capicua.checkWord("test"))
        self.assertFalse(capicua.checkWord("desktop"))


if __name__ == '__main__':
    unittest.main()
