from tree import *


def check_subtree(n1: BTNode, n2: BTNode):
    """Check if n2 is a subtree of n1 where both are binary trees."""
    # Solution: O(n) time where n is the number of nodes in n1.

    # Base case. Is n1 None or n2 None?
    if n1 is None or n2 is None:
        return False
    
    # Then we check recursively.
    if n1 is n2:
        return True
    return check_subtree(n1.left, n2) or check_subtree(n1.right, n2)


def check_subtree_only_data(n1: BTNode, n2: BTNode):
    """Check if n2 is a subtree of n1 where both are binary trees. 
    However, this time we are not allowed to use memory addresses to check, 
    only the node's data."""
    # Solution: O(n + km) time, where n is the number of nodes in n1 and m is the number of nodes in n2,
    # and k is the number of times that n2 appears in n1.

    # Base case. If n1 is None or n2 is None, then there should be no overlap.
    if n1 is None or n2 is None:
        return False
    
    # Then we check the node's data.
    if n1.data == n2.data and check_equal_tree(n1, n2):
        return True
    return check_subtree_only_data(n1.left, n2) or check_subtree_only_data(n1.right, n2)
        

def check_equal_tree(n1: BTNode, n2: BTNode):
    # Base case. Once we check both trees to the end, then they will be equal.
    if n1 is None and n2 is None:
        return True
    elif n1 is None or n2 is None:  # If one tree reaches the end first, then not equal.
        return False

    if n1.data != n2.data:
        return False
    return check_equal_tree(n1.left, n2.left) and check_equal_tree(n1.right, n2.right)