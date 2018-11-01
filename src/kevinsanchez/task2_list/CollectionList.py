from src.kevinsanchez.task2_list.Node import Node


class CollectionList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, data):
        new_node = Node(3)
        self.head.set_next_node(new_node)
        new_node.set_next_node(self.tail)

col = CollectionList()
print(col.head.get_next_node().get_data())
