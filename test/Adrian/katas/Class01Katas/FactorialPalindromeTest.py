from unittest import TestCase
from src.Adrian.katas.class01 import Class01Factorial
from src.Adrian.katas.class01 import Class01Palindrome


class FactorialPalindromeTest(TestCase):

    def test_factorial(self):
        self.assertEqual(120, Class01Factorial.factorial(6))

    def test_palindrome(self):
        self.assertEqual(True, Class01Palindrome.palindrome("oruro"))
