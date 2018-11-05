import unittest

from src.kevinh.katabank1.Collections.CollectionList import CollectionList


class TestCollectionList(unittest.TestCase):
    def setUp(self):
        self.collection_list = CollectionList()

    def test_append(self):
        self.collection_list.append(3)
        self.collection_list.append(4)
        self.assertEqual(2, len(self.collection_list))

    def test_get_element(self):
        self.collection_list.append(3)
        self.collection_list.append(4)
        self.collection_list.append(5)
        self.collection_list.append(6)
        self.assertEqual(3, self.collection_list[0])
        self.assertEqual(4, self.collection_list[1])

    def test_set_element_at_index(self):
        self.collection_list.append(3)
        self.collection_list.append(4)
        self.collection_list[0] = 5
        self.collection_list[1] = 100
        self.assertEqual(self.collection_list[0], 5)
        self.assertEqual(self.collection_list[1], 100)

    def test_for_iteration(self):
        self.collection_list.append(3)
        self.collection_list.append(4)
        collection = ""
        for value in self.collection_list:
            collection += str(value)
        self.assertEqual("34", collection)

    def test_print(self):
        self.collection_list.append(3)
        self.collection_list.append(4)
        self.assertEqual("[3, 4]", str(self.collection_list))
