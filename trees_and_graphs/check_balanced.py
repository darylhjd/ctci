from tree import *


def check_balanced(root: BTNode):
    """Check whether a binary tree is balanced (difference in height between left and right subtree
    is at most 1)"""
    # Solution: O(n) time for visiting every node, O(logn) space for recursive call.

    # The idea is to return a boolean indicating balanced tree and the max of left/right's depth.
    # Base case. If the root node is None, then it is already balanced.
    if root is None:
        return True, 0

    # Then, we check the depth for the left and right subtree
    left_balanced, left_depth = check_balanced(root.left)
    right_balanced, right_depth = check_balanced(root.right)
    return left_balanced and right_balanced and abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1
