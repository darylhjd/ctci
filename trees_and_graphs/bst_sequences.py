def bst_sequences(root):
    """Print all arrays that gives the provided tree."""
    # Solution: O(2^d) where d is the depth of the tree.

    if root is None:
        return []

    # Else, we get all possible sequences from the left and right tree.
    sequences = []
    left_ways = bst_sequences(root.left)
    right_ways = bst_sequences(root.right)
    if left_ways and right_ways:
        for left_way in left_ways:
            for right_way in right_ways:
                sequences.append([root.data] + left_way + right_way)
                sequences.append([root.data] + right_way + left_way)
    elif left_ways or right_ways:
        ways = left_ways if left_ways else right_ways
        for way in ways:
            sequences.append([root.data] + way)
    else:
        sequences.append([root.data])
    return sequences


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node: {self.data}"

    __repr__ = __str__


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right = Node(8)
    root.right.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)
    root.right.right.left.left = Node(12)
    root.right.right.left.right = Node(13)
    root.right.right.left.right.right = Node(14)

    print(bst_sequences(root))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)

    print(bst_sequences(root))
