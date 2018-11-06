from unittest import TestCase
from Adrian.kataList.KataList import KataList


class TestKataList(TestCase):

    def setUp(self):
        self.list_to_test = KataList()
        self.list_to_test.append(1)
        self.list_to_test.append(2)
        self.list_to_test.append('three')

    def test_len(self):
        self.assertEqual(len(self.list_to_test), 3)

    def test_iter(self):
        same = [1, 2, 'three']
        counter = 0
        for value in self.list_to_test:
            self.assertEqual(value, same[counter])
            counter += 1

    def test_insert(self):
        inserted = [1, 2, 3, 'three']
        counter = 0
        self.list_to_test.__print__()

        test = self.list_to_test.insert(1, 3)
        for value in self.list_to_test:
            self.assertEqual(value, inserted[counter])
            counter += 1

    def test_remove(self):
        removed = [1, 'three']
        counter = 0
        test = self.list_to_test.remove(2)
        for value in self.list_to_test:
            self.assertEqual(value, removed[counter])
            counter += 1
