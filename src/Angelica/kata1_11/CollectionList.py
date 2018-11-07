from src.Angelica.kata1_11.Node import Node

class CollectionList:

    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def __getitem__(self, item):
        if not self.head:
            return None
        else:
            iter_node = self.head
            pos = item
            while pos > 0 and iter_node.next:
                iter_node = iter_node.next
                pos -= 1
            return iter_node.next

    def __setitem__(self, key, value):
        pos = 0
        item = self.head
        while item is not None:
            if pos != key:
                item.next
                pos += 1
            else:
                item.next = value
                self.append(item)
                return

    def __len__(self):
        return self.length

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.length:
            item = self.head
            self.index += 1
            return item.next
        return self.head

    def remove(self,node):
        if node == None: return
        second = self.head
        node = second.next
        second.next = None
        return node

    def print_backward(self):
        print ("[")
        if self.head != None:
            self.head.print_backward()
        print ("]")

    def clear(self):
        self.head = None

