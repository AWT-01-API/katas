from unittest import TestCase
from Adrian.class01 import Kata1


class TestKata1(TestCase):
    kata1 = Kata1()

    def test_factorial(self):
        self.assertEqual(120, self.kata1.factorial(6))

    def test_palindrome(self):
        self.assertEqual(True, self.kata1.palindrome("oruro"))
