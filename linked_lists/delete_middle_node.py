from ll import *


def delete_middle_node(mnode: SLNode):
    """Delete the middle node from a singly linked list, given only that middle node."""
    # Solution: O(1) constant time.

    # First we need to check whether the length of the linked list is more than 2, since we are not
    # allowed to remove the first and last node.
    # However, we have to make some assumptions of the node that we have, that if the linked list were to have an
    # even number of nodes, then the node we are given is to the right of the linked list.

    # To check if the length of the linked list is more than 2, we check if the next node for the given node
    # is not None.
    if mnode is None or mnode.next is None:
        return

    # Now what we can do is we replace the data in the node to remove with that of the next node.
    # Then we replace the middle node's next node to mnode.next.next
    mnode.data = mnode.next.data
    mnode.next = mnode.next.next


if __name__ == '__main__':
    head = SLNode(0)
    temp = head

    num_nodes = 9
    middle_node = None
    for i in range(1, num_nodes):
        new_node = SLNode(i)
        if i == num_nodes // 2:
            middle_node = new_node
        temp.next = new_node
        temp = temp.next

    ll = SLL()
    ll.head = head
    ll.length = 9
    print(ll)
    delete_middle_node(middle_node)
    print(ll)
