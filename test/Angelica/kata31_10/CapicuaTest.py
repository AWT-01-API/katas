import unittest
from src.Angelica.kata31_10.Capicua import is_capicua


class TestCapicua(unittest.TestCase):

    def test_capicua(self):
        self.assertEqual(is_capicua("oruro"), True)

    def test_capicua_1(self):
        self.assertEqual(is_capicua("lapaz"), False)
