"""
Object type Node for Collection List.
"""


class Node:

    def __init__(self, start_data):
        self.data = start_data
        self.next_node = None
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
    Replace current data.
    """
    def set_data(self, new_data):
        self.data = new_data

    """
    Instances next node.
    """
    def set_next_node(self, new_node):
        self.next_node = new_node
