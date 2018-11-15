from src.kevinh.Kata1.Factorial import Factorial
import unittest


class TestFactorial(unittest.TestCase):

    def test_process_factorial(self):
        self.assertEqual(1, Factorial().process(1))
        self.assertEqual(2, Factorial().process(2))
        self.assertEqual(6, Factorial().process(3))
        self.assertEqual(24, Factorial().process(4))
        self.assertEqual(120, Factorial().process(5))
        self.assertEqual(87178291200, Factorial().process(14))
