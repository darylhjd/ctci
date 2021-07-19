from tree import *


def minimal_tree(array):
    """Generate a binary search tree with minimal height, given a sorted array of unique integers."""
    # Solution: O(n) time for going through each array element, O(logn) space for each recursive depth.

    # Terminal condition: If the array is empty, then return None
    if len(array) == 0:
        return None

    # Then we do something of a binary search.
    # We get the middle element and assign this element to this iteration's node.
    middle_index = len(array) // 2
    new_node = BTNode(array[middle_index])
    # Then we create the left and right side of the tree.
    new_node.left = minimal_tree(array[:middle_index])
    new_node.right = minimal_tree(array[middle_index+1:])
    return new_node
