from ll import *


def intersection(l1: SLL, l2: SLL):
    """Check whether two singly linked lists intersect each other by reference,
    and then return the intersecting node."""
    # Solution: O(n + m) time, where n and m are the lengths of the 2 linked lists,
    # O(n + m) space to store each reference for each node that we meet.

    # The idea is to link the tail of one of the lists to the head of the other list,
    # and then loop through until we meet the end of the list (None, which signifies no
    # inter), or a node that we have already met before, which will
    # be the intersecting node.

    visited = set()
    l1i = l1.head
    visited.add(l1i)
    while l1i.next:
        visited.add(l1i)
        l1i = l1i.next
    # At this point, l1i points to the tail of ll1.
    # Then, we join ll1's tail to ll2's head.
    l1i.next = l2.head
    while l1i:
        if l1i in visited:
            return l1i
        l1i = l1i.next
    return None


def intersection_no_buffer(l1, l2):
    """Check whether two singly linked lists intersect each other by reference,
    and then return the intersecting node, without using a buffer to store visited nodes."""
    # Solution: O(n + m) time, where n and m are the lengths of the 2 linked lists, O(1) auxiliary space.

    # We find the length of both lists, and advance the longer list by the difference.
    longer, shorter = (l1, l2) if len(l1) > len(l2) else (l2, l1)
    l_temp, s_temp = longer.head, shorter.head
    for _ in range(len(longer) - len(shorter)):
        l_temp = l_temp.next

    # Now we just loop through both longer and shorter and see whether they meet.
    while l_temp and s_temp:
        if l_temp is s_temp:
            return l_temp
        l_temp = l_temp.next
        s_temp = s_temp.next
    return None


if __name__ == '__main__':
    ll1 = SLL()
    inter = None
    temp = None
    for i in range(9):
        new_node = SLNode(i)
        if i == 4:
            inter = new_node
        if not ll1.head:
            ll1.head = new_node
            temp = ll1.head
        else:
            temp.next = new_node
            temp = temp.next

    print(inter)
    print(ll1)

    ll2 = SLL()
    temp = None
    for i in range(7):
        new_node = SLNode(i)
        if not ll2.head:
            ll2.head = new_node
            temp = ll2.head
        else:
            temp.next = new_node
            temp = temp.next
    print(ll2)
    temp.next = inter
    print("After appending to the end:")
    print(ll2)
    print(intersection_no_buffer(ll1, ll2))
