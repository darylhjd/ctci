from ll import *


def sum_lists(l1, l2):
    """Sum two lists whose numbers are stored in reverse order (1s-digit first) in a linked list, and store
    the result in a linked list in the same order."""
    # Solution: O(max(ll1, ll2)) time, O(1) space.
    new_ll = SLL()
    carry = 0
    onei = l1.head
    twoi = l2.head
    while carry or onei or twoi:
        total = carry + (onei.data if onei else 0) + (twoi.data if twoi else 0)
        carry, to_add = divmod(total, 10)
        new_ll.insert(to_add)
        onei = onei.next if onei else onei
        twoi = twoi.next if twoi else twoi
    return new_ll


def sum_lists_reversed(l1: SLL, l2: SLL):
    """Sum two lists whose numbers are stored in order in a linked list, and store
    the result in a linked list in the same order"""
    # Solution: O(max(ll1, ll2)) time to loop through each list.

    # Pad the shorter list with zeros at the beginning
    if l1.length >= l2.length:
        # Pad ll2 with zeros
        pad_zeros(l2, l1.length - l2.length)
    else:
        # Pad ll1 with zeros
        pad_zeros(l1, l2.length - l1.length)

    # Then we have to calculate the total manually.
    l1i = l1.head
    l2i = l2.head
    total = 0
    while l1i:
        total = total * 10 + l1i.data + l2i.data
        l1i = l1i.next
        l2i = l2i.next

    # Insert sum in order to a new linked list.
    new_ll = SLL()
    while total != 0:
        new_node = SLNode(total % 10)
        new_node.next = new_ll.head
        new_ll.head = new_node
        new_ll.length += 1
        total //= 10
    return new_ll


def pad_zeros(ll, n):
    """Pad a linked list with n zeros at the beginning"""
    for i in range(n):
        new_node = SLNode(0)
        new_node.next = ll.head
        ll.head = new_node
    ll.length += n


if __name__ == '__main__':
    ll1 = SLL()
    ll1.insert(0).insert(0).insert(5)
    ll2 = SLL()
    ll2.insert(0).insert(0).insert(5)
    print(f"Adding (reversed):\n{ll1} +\n{ll2}")
    ll3 = sum_lists(ll1, ll2)
    print("Result:")
    print(ll3)
    print()

    ll1 = SLL()
    ll1.insert(5).insert(0)
    ll2 = SLL()
    ll2.insert(5).insert(0).insert(0)
    print(f"Adding (in order):\n{ll1} +\n{ll2}")
    ll3 = sum_lists_reversed(ll1, ll2)
    print("Result:")
    print(ll3)

