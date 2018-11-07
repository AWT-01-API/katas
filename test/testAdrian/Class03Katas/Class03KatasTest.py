from Adrian.class03Katas import Class03Katas

from unittest import TestCase


class Class03(TestCase):

    def test_expanded_form(self):
        self.assertEqual(Class03Katas.Class03ExpandedForm.expanded_form(12), '10 + 2')
        self.assertEqual(Class03Katas.Class03ExpandedForm.expanded_form(42), '40 + 2')
        self.assertEqual(Class03Katas.Class03ExpandedForm.expanded_form(70304), '70000 + 300 + 4')

    def test_reverse_alternate(self):
        (Class03Katas.Class03ReverseAlternate.reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEqual(Class03Katas.Class03ReverseAlternate.reverse_alternate("I really hope it works this time..."),
                         "I yllaer hope ti works siht time...")
        self.assertEqual(Class03Katas.Class03ReverseAlternate.reverse_alternate("Reverse this string, please!"),
                         "Reverse siht string, !esaelp")
        self.assertEqual(Class03Katas.Class03ReverseAlternate.reverse_alternate("Have a beer"), "Have a beer")
        self.assertEqual(Class03Katas.Class03ReverseAlternate.reverse_alternate(""), "")
