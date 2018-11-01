import unittest
from src.Angelica.kata31_10.Factorial import factorial


class TestFactorialMethods(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_1(self):
        self.assertEqual(factorial(3), 6)

    if __name__ == '__main__':
        unittest.main()
