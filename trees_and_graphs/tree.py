class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BTNodeWithParent(BTNode):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbours = []
