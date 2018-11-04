from src.kevinsanchez.task2_list.Node import Node


"""
class with list I.
"""
class CollectionList(object):

    """
    constructor.
    """
    def __init__(self):
        self.head = None

    """
    method to if the list is empty.
    :return true or false.
    """
    def is_empty(self):
        return self.head is None

    """
    method to get the length of the list.
    :return length.
    """
    def __len__(self):
        counter = 0
        for value in self:
            counter += 1
        return counter

    """
    get a element in the given position.
    :return element
    """
    def __getitem__(self, item):
        if item < 0 or item > self.__len__():
            return None
        else:
            pt = self.head
            if item is 0:
                return pt.get_data()
            counter = 0
            while (pt.get_next_node() is not None) and (item is not counter):
                counter += 1
                pt = pt.get_next_node()
            return pt.get_data()

    """
    set an element in a given position.
    """
    def __setitem__(self, key, value):
        if 0 <= key <= self.__len__():
            pt = self.head
            if key is 0:
                pt.set_data(value)
            counter = 0
            while (pt.next_node is not None) and (key is not counter):
                counter += 1
                pt = pt.get_next_node()
            pt.set_data(value)

    """
    insert an element at the end.
    """
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            pt = self.head
            while pt.get_next_node() is not None:
                pt = pt.get_next_node()
            pt.set_next_node(new_node)

    """
    itertor.
    """
    def __iter__(self):
        self.helper_node = self.head
        self.i = 0
        return self

    """
    rule for loop.
    """
    def next(self):
        if self.helper_node.get_next_node() is None:
            raise StopIteration
        else:
            if self.i is 0:
                self.i = 1
                return self.helper_node.get_data()
            else:
                self.helper_node = self.helper_node.get_next_node()
                return self.helper_node.get_data()
