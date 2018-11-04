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
        if not self.is_empty():
            for value in self:
                counter += 1
        return counter

    """
    get a element in the given position.
    :return element.
    """
    def __getitem__(self, item):
        if self.is_empty():
            return None
        if 0 <= item <= self.__len__():
            helper = self.head
            if item is 0:
                return helper.get_data()
            counter = 0
            while (helper.get_next_node() is not None) and (item is not counter):
                counter += 1
                helper = helper.get_next_node()
            return helper.get_data()

    """
    set an element in a given position.
    :param key position.
    :param value.
    """
    def __setitem__(self, key, value):
        if self.is_empty():
            return None
        if 0 <= key <= self.__len__():
            helper = self.head
            if key is 0:
                helper.set_data(value)
            counter = 0
            while (helper.next_node is not None) and (key is not counter):
                counter += 1
                helper = helper.get_next_node()
            helper.set_data(value)

    """
    insert an element at the end.
    :param value.
    """
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            helper = self.head
            while helper.get_next_node() is not None:
                helper = helper.get_next_node()
            helper.set_next_node(new_node)

    """
    itertor.
    """
    def __iter__(self):
        self.helper_node = self.head
        self.i = 0
        return self

    """
    rule for loop.
    :return next data.
    """
    def next(self):
        if self.is_empty():
            raise StopIteration
        if self.helper_node.get_next_node() is None:
            raise StopIteration
        else:
            if self.i is 0:
                self.i = 1
                return self.helper_node.get_data()
            else:
                self.helper_node = self.helper_node.get_next_node()
                return self.helper_node.get_data()

    """
    method which insert a vale
    in the given position.
    :param position
    :param value
    """
    def insert(self, position, value):
        counter = 1
        new_node = Node(value)
        if self.is_empty():
            return None
        elif position is 0:
            helper_head = self.head
            self.head = new_node
            new_node.set_next_node(helper_head)
        else:
            helper_node = self.head
            while (helper_node.get_next_node() is not None) and (counter is not position):
                helper_node = helper_node.get_next_node()
                counter += 1
            new_node.set_next_node(helper_node.get_next_node())
            helper_node.set_next_node(new_node)

    """
    clear method.
    """
    def clear(self):
        self.head = None
