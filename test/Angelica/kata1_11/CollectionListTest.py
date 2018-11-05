import unittest
from src.Angelica.kata1_11.CollectionList import CollectionList


class CollectionListTest(unittest.TestCase):

    def setUp(self):
        self.collection_list = CollectionList()
        self.collection_list.append(3)
        self.collection_list.append(2)

    def test_len(self):
        print(len(self.collection_list))
        self.assertEqual(len(self.collection_list), 1)
