import unittest
from src.kevinsanchez.task5_11_14_2018.DashatizeIt import DashatizeIt

"""
class for test dasharize.
"""
class TestDasharize(unittest.TestCase):

    """
    test method dasharize.
    """
    def test_dasharize(self):
        self.assertEqual("2-7-4", DashatizeIt.dashatize(274), "Should return 2-7-4")
        self.assertEqual("5-3-1-1", DashatizeIt.dashatize(5311), "Should return 5-3-1-1")
        self.assertEqual("86-3-20", DashatizeIt.dashatize(86320), "Should return 86-3-20")
        self.assertEqual("9-7-4-3-02", DashatizeIt.dashatize(974302), "Should return 9-7-4-3-02")
        self.assertEqual("None", DashatizeIt.dashatize(None), "Should return None");
        self.assertEqual("0", DashatizeIt.dashatize(0), "Should return 0");
        self.assertEqual("1", DashatizeIt.dashatize(-1), "Should return 1");
        self.assertEqual("28-3-6-9", DashatizeIt.dashatize(-28369), "Should return 28-3-6-9");