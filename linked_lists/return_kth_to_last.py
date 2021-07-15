from ll import *


def return_kth_to_last(head_node: SLNode, k: int):
    """Return the kth to last element from a singly linked list."""
    # Solution: O(n) to loop through the entire linked list to find the end.

    if k < 0:
        return None

    # Advance last_finder forward k times.
    # If we meet the end of the list before k times, then there means there is no kth item from last.
    last_finder = head_node
    kth_last = None
    for i in range(k):
        if last_finder.next is None:
            return None
        last_finder = last_finder.next

    # At this point, set kth_last to the head_node. kth_last will be the kth element from last_finder.
    # Then loop both last_finder and kth_last forward until last_finder is the last node.
    kth_last = head_node
    while True:
        if last_finder.next is None:
            break
        last_finder = last_finder.next
        kth_last = kth_last.next
    return kth_last


if __name__ == '__main__':
    ll = SLL()
    ll.insert(1).insert(2).insert(3).insert(4).insert(5).insert(1).insert(5)
    print(ll)
    k_last = return_kth_to_last(ll.head, 3)
    print(f"3rd from last is {k_last.data}")
    assert k_last.data == 4

    k_last = return_kth_to_last(ll.head, 6)
    print(f"6th from last is {k_last.data}")
    assert k_last.data == 1

    k_last = return_kth_to_last(ll.head, 7)
    print(f"7th from last is {k_last}")
    assert k_last is None

    k_last = return_kth_to_last(ll.head, 0)
    print(f"0th from last is {k_last.data}")
    assert k_last.data == 5
