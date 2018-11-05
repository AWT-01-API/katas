from unittest import TestCase
from Adrian.class01.Class01 import Class01


class TestKata1(TestCase):

    def test_factorial(self):
        self.assertEqual(120, Class01.factorial(6))

    def test_palindrome(self):
        self.assertEqual(True, Class01.palindrome("oruro"))
