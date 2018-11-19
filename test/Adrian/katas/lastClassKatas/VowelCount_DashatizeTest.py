from unittest import TestCase
from src.Adrian.katas.lastClassKatas.VowelCount_Dashatize import VowelCount
from src.Adrian.katas.lastClassKatas.VowelCount_Dashatize import Dashatize

class TestKataList(TestCase):

    def test_vowel_count(self):
        self.assertEqual(VowelCount.get_count("abracadabra"), 5)

    def test_dashatize(self):
        self.assertEqual(Dashatize.dashatize(274), "2-7-4", "Should return 2-7-4")
        self.assertEqual(Dashatize.dashatize(5311), "5-3-1-1", "Should return 5-3-1-1")
        self.assertEqual(Dashatize.dashatize(86320), "86-3-20", "Should return 86-3-20")
        self.assertEqual(Dashatize.dashatize(974302), "9-7-4-3-02", "Should return 9-7-4-3-02")
        self.assertEqual(Dashatize.dashatize(None), "None", "Should return None");
        self.assertEqual(Dashatize.dashatize(0), "0", "Should return 0");
        self.assertEqual(Dashatize.dashatize(-1), "1", "Should return 1");
        self.assertEqual(Dashatize.dashatize(-28369), "28-3-6-9", "Should return 28-3-6-9");