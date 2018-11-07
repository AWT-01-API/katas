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
        self.collection_list.append(7)
        self.collection_list.append(1)

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
        self.assertEqual(7, element)

        element = self.collection_list[0]
        self.assertEqual(3, element)

        element = self.collection_list[2]
        self.assertEqual(1, element)

        self.collection_list[0] = 4
        element = self.collection_list[0]
        self.assertEqual(4, element)

    """
    check iteraror.
    """
    def test_get(self):
        list = [3, 7, 1]
        counter = 0
        for value in self.collection_list:
            self.assertEqual(value, list[counter])
            counter += 1

    """
    test insert.
    """
    def test_insert(self):
        self.collection_list.insert(0, 10)
        self.assertEqual(10, self.collection_list[0])

    """
    test method clear.
    """
    def test_clear(self):
        self.collection_list.clear()
        self.assertEqual(0, len(self.collection_list))
        self.assertTrue(self.collection_list.is_empty())

    """
    test method remove.
    """
    def test_remove(self):
        self.collection_list.append("deleted")
        self.assertEqual("deleted", self.collection_list.remove("deleted").get_data())

    """
    test method to print.
    """
    def test_print(self):
        print (self.collection_list)

    """
    test method count.
    """
    def test_count(self):
        self.collection_list.append(3)
        self.assertEqual(2, self.collection_list.count(3))
    """
    still testing.
    """
    def test_reverse(self):
        print (self.collection_list)
        self.collection_list.reverse()
        print (self.collection_list)
