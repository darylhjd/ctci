from ll import *


def palindrome(ll):
    """Check whether a linked list is a palindrome"""
    # Solution: O(n) time for iterating through the linked list, O(n) space for storing buffer of characters

    # What we do is we create a new linked list as we iterate through the original, but this time each new
    # character is added to the front of the new linked list. We only do this for half of the linked list.

    buffer_ll = SLL()
    # Loop until half way through the original ll.
    temp = ll.head
    for i in range(ll.length // 2):
        buffer_ll.insert_beginning(temp.data)
        temp = temp.next

    # Advance to the next node.
    temp = temp.next
    # If length is odd, we advance once more.
    if ll.length % 2:
        temp = temp.next

    # Then we loop through the rest of the original ll and check against each buffer.
    # Note that since the buffer nodes were added backwards, so we can just iterate through and check for each.
    b_temp = buffer_ll.head
    while temp:
        if temp.data != b_temp.data:
            return False
        temp = temp.next
        b_temp = b_temp.next
    return True


if __name__ == '__main__':
    l = SLL()
    for c in "racecar":
        l.insert(c)
    print(l)
    assert palindrome(l)

    l = SLL()
    for c in "carrac":
        l.insert(c)
    print(l)
    assert palindrome(l)

    l = SLL()
    for c in "not":
        l.insert(c)
    print(l)
    assert not palindrome(l)
