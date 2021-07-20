class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node: {self.data}"

    __repr__ = __str__


class BTNodeWithParent(BTNode):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbours = []
