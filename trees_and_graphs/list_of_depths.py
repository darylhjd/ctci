from tree import *


def list_of_depths(root: BTNode):
    """Create a new linked list of all nodes at each depth, and return all the linked lists."""
    # Solution: O(n) time for going through each node, O(n) space for storing the linked lists.

    # Create a list to store all the linked lists.
    lls = []
    if root is None:
        return lls

    # We use 2 separate queues and interchange them for each iteration.
    aux_1 = [root]
    aux_2 = []
    while len(aux_1) != 0:
        # Append the current depth to the linked lists list.
        lls.append(aux_1)
        # Then for each node, we append their neighbours to the other auxiliary list.
        for node in aux_1:
            if node.left is not None:
                aux_2.append(node.left)
            if node.right is not None:
                aux_2.append(node.right)
        # Then we replace aux_1 with aux_2 and empty aux_2 to let the cycle repeat.
        aux_1 = aux_2
        aux_2 = []
    return lls
