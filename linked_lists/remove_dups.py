from ll import *


def remove_dups(head_node: SLNode):
    """Remove duplicate entries from a singly linked list."""
    # Solution: O(n) time for iterating through linked list once and O(n) for storing unique data.

    # Create set to store any data that we meet.
    visited = set()

    prev = head_node
    visited.add(prev.data)
    nex = prev.next
    while nex is not None:
        if nex.data in visited:
            prev.next = nex.next
        else:
            visited.add(nex.data)
            prev = nex
        nex = nex.next


def remove_dups_no_buffer(head_node: SLNode):
    """Remove duplicate entries from a singly linked list without an extra buffer"""
    # Solution: O(n^2) time for iterating through linked list for each node, and then iterating the whole linked list
    # to find occurences for that node.

    # What we can do is for each node, we loop through the remaining nodes to see if
    # there are any occurences for that node.
    selector = head_node
    while selector is not None:
        prev = selector
        nex = prev.next
        while nex is not None:
            if nex.data == selector.data:
                prev.next = nex.next
            else:
                prev = nex
            nex = nex.next
        selector = selector.next


if __name__ == '__main__':
    ll = SLL()
    ll.insert(1).insert(2).insert(3).insert(4).insert(5).insert(1).insert(5)
    print(ll)
    remove_dups(ll.head)
    print(ll)

    ll = SLL()
    ll.insert(1).insert(2).insert(3).insert(4).insert(5).insert(1).insert(5)
    print(ll)
    remove_dups_no_buffer(ll.head)
    print(ll)
