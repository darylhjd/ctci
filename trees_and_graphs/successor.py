from tree import *


def successor(node: BTNodeWithParent):
    """Find the in-order successor of a node in a binary search tree."""
    # Solution: O(n) time for going through nodes in the tree. O(1) space.

    # To find the next successor in a binary search tree,
    # we need to find the min node on the right side of the tree.
    # If the right side of the tree is None,
    # then we gotta find the successor through the parent.
    # If the parent's left node is the current node, then the parent is the successor.
    # If the parent's right node is the current node, we need to iterate until the prev node is a left node,
    # then we go down the right side and find the left most node.
    # If both are none, then there is no successor to the node.

    # If node is None, there is no successor.
    if node is None:
        return None

    if node.right:
        return get_right_subtree_left_most(node)
    elif node.parent:
        child = node
        parent = node.parent
        while parent and parent.left != child:
            child = parent
            parent = parent.parent
        return parent
    else:
        return None


def get_right_subtree_left_most(parent_node):
    temp = parent_node.right
    while temp and temp.left:
        temp = temp.left
    return temp
