from ll import *


def loop_detection(ll):
    """Detect the node at the beginning of the loop and return it."""
    # Solution: ?

    # We create a slow and fast pointer, where the slow pointer just advances once
    # while the fast pointer advances twice for each tick.
    slow = fast = ll.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    # Then we move slow back to the start
    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':
    middle_node = None
    l = SLL()
    temp = None
    for i in range(7):
        new_node = SLNode(i)
        if i == 5:
            middle_node = new_node
        if not l.head:
            l.head = new_node
            temp = new_node
        else:
            temp.next = new_node
            temp = temp.next

    temp.next = middle_node
    print(loop_detection(l))
