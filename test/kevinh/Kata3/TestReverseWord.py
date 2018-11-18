from src.kevinh.Kata3.ReverseWord import ReverseWord
import unittest


class TestFactorial(unittest.TestCase):
    def test_reverse_other_words(self):
        self.assertEqual(ReverseWord.reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEqual(ReverseWord.reverse_alternate("I really hope it works this time..."),"I yllaer hope ti works siht time...")
        self.assertEqual(ReverseWord.reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
        self.assertEqual(ReverseWord.reverse_alternate("Have a beer"), "Have a beer")
        self.assertEqual(ReverseWord.reverse_alternate("   "), "")
        self.assertEqual(ReverseWord.reverse_alternate("This is not a test "), "This si not a test")
        self.assertEqual(ReverseWord.reverse_alternate("This       is a  test "), "This si a tset")
