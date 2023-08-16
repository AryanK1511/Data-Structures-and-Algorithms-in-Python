class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node
        if not current_node:
            self.head_node = new_node
            return
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def __iter__(self):
        current_node = self.head_node
        while current_node:
            yield current_node.value
            current_node = current_node.next_node