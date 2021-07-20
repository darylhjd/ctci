from tree import *


def first_common_ancestor(n1, n2):
    """Find the first common ancestor for 2 nodes in a binary tree.
    Avoid storing additional nodes in any data structure."""
    # Solution: O(n) to go through all nodes.

    parent = n1
    prev = None
    while parent:
        # Check parent itself
        if dfs(parent, n2):
            return parent

        # Check parent's left.
        if parent.left is not prev:
            if dfs(parent.left, n2):
                return parent.left

        # Check parent's right.
        if parent.right is not prev:
            if dfs(parent.right, n2):
                return parent.right

        # Then move up.
        prev = parent
        parent = parent.parent


def dfs(n1, n2):
    """Return true if n2 is within n1's subtree."""
    if not n1 or not n2:
        return False
    elif n1 is n2:
        return True

    return dfs(n1.left, n2) or dfs(n1.right, n2)


def first_common_ancestor_no_parent(root, n1, n2):
    """Find the first common ancestor of n1 and n2.
    This time, we assume that we are unable to get the parent for each node, but
    we are given the root node of the tree."""

    # To see if a node contains the required ancestor, we can use a helper function.
    # The helper function returns the number of nodes that are found on that side of the subtree.
    # For example, if node.left contains both n1 and n2, then it will return 2, while if it finds
    # only one of the 2, it will return 1.

    # Base case. If the root is n1 or n2, then it must be the ancestor.
    if root is n1 or root is n2:
        return root
    elif n1 is n2:
        return n1
    else:
        return dfs_number_return(root, n1, n2)


def dfs_number_return(root, n1, n2):
    if root is None:
        return None, 0

    # If this node is n1 or n2, then we add one.
    result = 1 if root is n1 or root is n2 else 0
    left_result, left_num = dfs_number_return(root.left, n1, n2)
    if left_result:
        return left_result, 2
    elif result + left_num == 2:
        return root, 2
    right_result, right_num = dfs_number_return(root.right, n1, n2)
    if right_result:
        return right_result, 2

    result += left_num + right_num
    if result == 2:
        return root, 2
    return None, result



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

    print(first_common_ancestor_no_parent(root, root.right.right.left.left, root.right.right.left.right.right))
