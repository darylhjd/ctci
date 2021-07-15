# This file includes an implementation of a linked list in Python
class SLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node: {self.data} at {id(self)}"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self is other and self.data == other.data

    def __hash__(self):
        return hash((self.data, id(self.next)))


class SLL:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = SLNode(data)
        if self.head is None:
            self.head = new_node
            return self

        prev = None
        temp = self.head
        while temp:
            prev = temp
            temp = temp.next
        prev.next = new_node

        self.length += 1
        return self

    def insert_beginning(self, data):
        new_node = SLNode(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def __str__(self):
        d = []
        temp = self.head
        while temp is not None:
            d.append(str(temp.data))
            temp = temp.next
        d.append("None")
        return " -> ".join(d)

    def __len__(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length


class DLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
