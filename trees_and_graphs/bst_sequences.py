from tree import *


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


if __name__ == '__main__':
    root = BTNode(5)
    root.left = BTNode(4)
    root.left.left = BTNode(3)
    root.left.right = BTNode(2)
    root.right = BTNode(8)
    root.right.right = BTNode(9)
    root.right.right.left = BTNode(10)
    root.right.right.right = BTNode(11)
    root.right.right.left.left = BTNode(12)
    root.right.right.left.right = BTNode(13)
    root.right.right.left.right.right = BTNode(14)

    print(bst_sequences(root))

    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.right = BTNode(4)
    root.left.left = BTNode(5)

    print(bst_sequences(root))
