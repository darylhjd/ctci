from ll import *


def partition(ll: SLL, v):
    """Partition a linked list into 2 parts, with nodes less than v on the left side and nodes equal or
    more than v on the right side."""
    # Solution: O(n) to loop through the linked list, and O(1) space.

    # We can use another variable to keep track of the nodes that are >= v.
    more_nodes = None
    less_nodes = None

    # Then we loop through the whole list, and insert nodes which are >= v into more_nodes.
    prev = None
    nex = ll.head
    while nex is not None:
        if nex.data >= v:
            temp = nex
            nex = nex.next
            temp.next = more_nodes
            more_nodes = temp
            if prev is not None:
                prev.next = nex
        else:
            if less_nodes is None:
                less_nodes = nex
            prev = nex
            nex = nex.next

    # Then we join back more_nodes back into the main list
    if prev is None:
        ll.head = more_nodes
    else:
        prev.next = more_nodes
        ll.head = less_nodes


if __name__ == '__main__':
    ll = SLL()
    ll.insert(1).insert(2).insert(10).insert(5).insert(8).insert(5).insert(3)
    print(ll)
    partition(ll, 5)
    print(ll)
