from tree import *


def validate_bst(root: BTNode, mi, ma):
    """Validate whether a binary tree is a binary search tree."""
    # Solution: O(n) time for going through each node, O(logn) for recursive calling.

    # Base case. If the root is None, return True.
    if root is None:
        return True

    # We check if current node satisfies bounds. The current node's value
    # must be equal to or more than mi, and less than ma.
    if not mi <= root.data < ma:
        return False
    else:
        return validate_bst(root.left, mi, root.data) and validate_bst(root.right, root.data, ma)
