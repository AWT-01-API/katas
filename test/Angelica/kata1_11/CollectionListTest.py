import unittest
from src.Angelica.kata1_11.CollectionList import CollectionList


class CollectionListTest(unittest.TestCase):

    def setUp(self):
        self.collection_list = CollectionList()
        self.collection_list.append(3)
        self.collection_list.append(2)

    def test_get_first_element(self):
        firts_element = self.collection_list[0]
        print(firts_element)

    def test_len(self):
        print(len(self.collection_list))
        self.assertEqual(len(self.collection_list), 2)

    def test_get_second_element(self):
        self.collection_list[1] = 100
        second_element = self.collection_list[1]
        print(second_element)
        self.assertEqual(100, second_element)

    def test_it_for(self):
        for value in self.collection_list:
            print(value)

    def test_print_format(self):
        self.collection_list.print_backward()

    def test_print_format(self):
        actual = self.collection_list.remove(2)
        self.assertEqual(str(3), str(actual))