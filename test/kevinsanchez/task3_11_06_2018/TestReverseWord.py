import unittest
from src.kevinsanchez.task3_11_06_2018.ReverseWord import ReverseWord

"""
test class for reverse.
"""
class TestReverseWord(unittest.TestCase):

    """
    set up for test.
    """
    def setUp(self):
        self.reverse_word = ReverseWord()

    """
    test for revert method.
    """
    def test_revert(self):
        self.assertEquals(self.reverse_word.reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEquals(self.reverse_word.reverse_alternate("I really hope it works this time..."),
                          "I yllaer hope ti works siht time...")
        self.assertEquals(self.reverse_word.reverse_alternate("Reverse this string, please!"),
                          "Reverse siht string, !esaelp")
        self.assertEquals(self.reverse_word.reverse_alternate("Have a beer"), "Have a beer")
        self.assertEquals(self.reverse_word.reverse_alternate(""), "")
