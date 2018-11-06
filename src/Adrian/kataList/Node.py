"""
Object type Node for Collection List.
"""


class Node:

    def __init__(self, start_data):
        self.data = start_data
        self.next_node = None
        self.previous_node = None
        self.index = 0
    """
    Get Node data.
    """
    def get_data(self):
        return self.data
    """
    Get next Node data.
    """
    def get_next_node(self):
        return self.next_node

    """
    Get previous Node data.
    """
    def get_prev_node(self):
        return self.previous_node

    """
    Replace current data.
    """
    def set_data(self, new_data):
        self.data = new_data

    """
    Instances next node.
    """
    def set_next_node(self, new_node):
        self.next_node = new_node
