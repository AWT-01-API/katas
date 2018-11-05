import unittest

from src.Angelica.kata1_11.CollectionList import CollectionList


class CollectionList(unittest.TestCase):
    def test_init(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        print(len(collection_list))
        self.assertEqual(len(collection_list), 2)

    def test_getElement(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        first_element = collection_list.get_index(0)
        print(first_element)
        self.assertEqual(first_element, 3)
