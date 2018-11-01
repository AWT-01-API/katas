import unittest
from src.Angelica.kata31_10.Capicua import is_capicua


class TestFactorialMethods(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(is_capicua("oruro"), True)

    def test_factorial_1(self):
        self.assertEqual(is_capicua("lapaz"), False)

    if __name__ == '__main__':
        unittest.main()
