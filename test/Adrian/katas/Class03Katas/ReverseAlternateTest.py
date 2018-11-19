from src.Adrian.katas.class03Katas.Class03 import Class03ReverseAlternate

from unittest import TestCase


class Class03(TestCase):

    def ReverseAlternateTest(self):
        (Class03ReverseAlternate.reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEqual(Class03ReverseAlternate.reverse_alternate("I really hope it works this time..."),
                         "I yllaer hope ti works siht time...")
        self.assertEqual(Class03ReverseAlternate.reverse_alternate("Reverse this string, please!"),
                         "Reverse siht string, !esaelp")
        self.assertEqual(Class03ReverseAlternate.reverse_alternate("Have a beer"), "Have a beer")
        self.assertEqual(Class03ReverseAlternate.reverse_alternate(""), "")
