from Adrian.kataList.Node import Node

"""
Kata list.
"""


class KataList (object):

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
            for self.index in self:
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
            self.index = 1
        else:
            element = self.head
            while element.get_next_node() is not None:
                element = element.get_next_node()
            element.set_next_node(new_node)
            element.index += 1
            new_element = element.get_next_node()
            new_element.set_prev_node(element)

    """
    STAGE 2.
    Return an element of a given position.
    """
    def __getitem__(self, position):
        if self.is_empty():
            return None
        if type(position) is not int:
            raise KeyError
        if 0 <= position <= len(self):
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
        elif self.index is 0:
            self.index = 1
            return self.element.get_data()
        else:
            self.element = self.element.get_next_node()
            return self.element.get_data()

    """
    Rule for iterator previous.
    """

    def prev(self):
        if self.is_empty() or (self.element.get_prev_node() is None):
            raise StopIteration
        else:
            if self.index is 0:
                raise StopIteration
            else:
                self.element = self.element.get_prev_node()
                return self.element.get_data()
    """
    STAGE 5:
    Insert an element in between the list
    """
    def insert(self, position, value):
        new_element = Node(value)
        current_element = self.head
        if self.is_empty() or position > len(self):
            raise OverflowError
        elif position == 0:
            self.head = new_element
            new_element.set_next_node(current_element)
        else:
            counter = 0
            while (current_element.get_next_node() is not None) and (counter is not position):
                current_element = current_element.get_next_node()
                counter += 1
            new_element.set_next_node(current_element.get_next_node())
            current_element.set_next_node(new_element)

    """
    STAGE 6:
    Remove an element from a given position
    """
    def remove(self, element):

        current_element = self.head
        if self.is_empty():
            raise OverflowError("List is empty")
        elif len(self) == 1:
            self.clear()
        else:
            while current_element.get_next_node() is not None:
                current_element = current_element.get_next_node()
                if current_element.get_data() == element:
                    new_next_element = current_element.get_next_node()
                    current_element = current_element.get_prev_node()
                    current_element.set_next_node(new_next_element)
                    break

    """
    Stage 7:
    Clears the list
    """
    def clear(self):
        self.head = None

    """
    Formats the list
    """
    def formatted(self):

        formatted = '['
        i = 0
        k = len(self)
        for value in self:
            formatted += str(value)
            if i < k - 1:
                formatted += ', '
            i += 1
        formatted += ']'
        return formatted

    """
    Stage 8:
    Print list
    """
    def __print__(self):
        print self.formatted()

    """
    Stage 9:
    Reverse list
    """
    def reverse(self):
        last_element = self.head
        reversed_list = KataList()
        if self.is_empty():
            raise OverflowError("List is empty")
        else:
            while last_element.get_next_node() is not None:
                last_element.get_next_node()
            while last_element.get_prev_node() is not None:
                reversed_list.append(last_element.get_data())
                last_element.get_prev_node()
        return reversed_list
