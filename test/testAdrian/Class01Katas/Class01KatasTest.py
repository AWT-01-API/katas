from unittest import TestCase
from Adrian.class01.Class01Katas import Class01Factorial
from Adrian.class01.Class01Katas import Class01Palindrome


class TestKata1(TestCase):

    def test_factorial(self):
        self.assertEqual(120, Class01Factorial.factorial(6))

    def test_palindrome(self):
        self.assertEqual(True, Class01Palindrome.palindrome("oruro"))
