from unittest import TestCase
from Adrian.kataList.KataList import KataList


class TestKataList(TestCase):

    def set_list(self):
        self.collection = KataList
        self.collection.append(1)
        self.collection.append(2)


    def test_len(self):
        self.assertEqual(len(self.collection),2)

    def test_iter(self):
        same = [1,2]
        counter = 0
        for value in self.collection:
            self.assertEqual(value, same[counter])
            counter += 1
