from unittest import TestCase
from src.Adrian.kataList.KataList import KataList


class TestKataList(TestCase):

    def setUp(self):
        self.list_to_test = KataList()
        self.list_to_test.append(1)
        self.list_to_test.append(2)
        self.list_to_test.append("'three'")

    def test_len(self):
        self.assertEqual(len(self.list_to_test), 3)

    def test_insert(self):
        inserted = [1, 2, 3, 'three']
        self.list_to_test.__print__()
        self.list_to_test.insert(1, 3)
        self.assertEqual(str(inserted), self.list_to_test.formatted())

    def test_remove(self):
        removed = [1, 'three']
        self.list_to_test.remove(2)
        self.assertEqual(self.list_to_test.formatted(), str(removed))

    def test_reverse(self):
        reversed_list = ['three', 2, 1]
        self.list_to_test = self.list_to_test.reverse()
        self.assertEqual(self.list_to_test.formatted(), str(reversed_list))

    def test_count(self):
        self.assertEqual(1, self.list_to_test.count(2))

