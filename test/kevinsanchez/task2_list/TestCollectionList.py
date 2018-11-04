import unittest
from src.kevinsanchez.task2_list.CollectionList import CollectionList


"""
class for test collectionlist class.
"""
class TestCollectionList(unittest.TestCase):

    """
    set up for the test.
    """
    def setUp(self):
        self.collection_list = CollectionList()
        self.collection_list.append(3)
        self.collection_list.append("QQQQ")
        self.collection_list.append([1, 2])

    """
    test function len.
    """
    def test_len(self):
        self.assertEqual(len(self.collection_list), 3)

    """
    method to check position of elements get and set.
    """
    def test_check_elemet(self):
        element = self.collection_list[1]
        self.assertEqual("QQQQ", element)

        element = self.collection_list[0]
        self.assertEqual(3, element)

        element = self.collection_list[2]
        self.assertEqual([1, 2], element)

        self.collection_list[0] = 7
        element = self.collection_list[0]
        self.assertEqual(7, element)

    """
    check iteraror.
    """
    def test_get(self):
        list = [3, "QQQQ", [1, 2]]
        counter = 0
        for value in self.collection_list:
            self.assertEqual(value, list[counter])
            counter += 1
