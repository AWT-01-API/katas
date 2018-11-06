class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.index = 0
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def get_index(self):
        return self.index

    def set_data(self, new_data):
        self.data = new_data

    def set_next_node(self, new_node):
        self.next_node = new_node

    def set_index(self, new_index):
        self.index = new_index