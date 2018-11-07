class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return str(self.item)

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print(self.item,)
