from Adrian.kataList.Node import Node

"""
Kata list.
"""


class KataList:

    def __init__(self):
        self.head = None
        self.element = None
        self.index = 0

    """
    Return true if the list is not empty
    """
    def is_empty(self):
        return self.head is None

    """
    STAGE 1.
    Return length of list. 
    """
    def __len__(self):
        counter = 0
        if not self.is_empty():
            for val in self:
                counter += 1
        return counter
    """
    STAGE 1.
    Add a new element at the end.
    """

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            element = self.head
            while element.get_next_node() is not None:
                element = element.get_next_node()
            element.set_next_node(new_node)

    """
    STAGE 2.
    Return an element of a given position.
    """
    def __getitem__(self, position):
        if self.is_empty():
            return None
        if type(position) is not int:
            raise KeyError
        if 0 <= position <= self.__len__():
            element = self.head
            if position is 0:
                return element
            counter = 0
            while (element.get_next_node() is not None) and (position is not counter):
                counter += 1
                element = element.get_next_node()
            return element
        else:
            raise OverflowError("InvalidRangeError")

    """
    STAGE 3.
    Set an element of a given position.
    """
    def __setitem__(self, position, value):
        item = self.__getitem__(position)
        item.set_data(value)

    """
    STAGE 4:
    Iterator to return itself.
    """

    def __iter__(self):
        self.element = self.head
        self.index = 0
        return self

    """
    STAGE 4.
    Rule for iterator next.
    """

    def next(self):
        if self.is_empty() or (self.element.get_next_node() is None):
            raise StopIteration
        else:
            if self.index is 0:
                self.index += 1
                return self.element.get_data()
            else:
                self.element = self.element.get_next_node()
                return self.element.get_data()


