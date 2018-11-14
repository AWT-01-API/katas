import unittest
from src.kevinsanchez.task5_11_14_2018.VowelCount import VowelCount

"""
test class.
"""


class TestVowelCount(unittest.TestCase):
    """
    test for get_count.
    """

    def test_count(self):
        self.assertEqual(5, VowelCount.get_count('abracadabra'))
