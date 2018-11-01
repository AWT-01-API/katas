import unittest

from src.kevinh.katabank1.Collections.CollectionList import CollectionList


class TestCollectionList(unittest.TestCase):

    def test_append(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        self.assertEqual(2, len(collection_list))

    def test_getElement(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        self.assertEqual(3, collection_list[0])
        self.assertEqual(4, collection_list[1])

    def test_setElementAtIndex(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        collection_list[1] = 100
        self.assertEqual(collection_list[1], 100)

    def test_For_Iteration(self):
        collection_list = CollectionList()
        collection_list.append(3)
        collection_list.append(4)
        collection = ""
        for value in collection_list:
            collection += str(value)
        self.assertEqual(collection, "34")


if __name__ == '__main__':
    unittest.main()
