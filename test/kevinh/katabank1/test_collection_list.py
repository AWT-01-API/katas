import unittest

from src.kevinh.katabank1.Collections.CollectionList import CollectionList


class TestCollectionList(unittest.TestCase):

    def test_append(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        self.assertEqual(2, len(collection_list))

    def test_get_element(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        collection_list.append(5)
        collection_list.append(6)
        self.assertEqual(3, collection_list[0])
        self.assertEqual(4, collection_list[1])

    def test_set_element_at_index(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        collection_list[1] = 100
        collection_list[0] = 5
        self.assertEqual(collection_list[0], 5)
        self.assertEqual(collection_list[1], 100)

    def test_for_iteration(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        collection = ""
        for value in collection_list:
            collection += str(value)
        self.assertEqual("34", collection)


if __name__ == '__main__':
    unittest.main()
