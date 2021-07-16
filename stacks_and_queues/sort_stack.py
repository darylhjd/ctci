import random

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


def sort_stack(s: Stack):
    """Sort a stack with the smallest elements at the top."""
    # Solution: O(n^2) time if the original stack was in reversed sorted order, O(n) extra space.
    # Return if stack is empty.
    if len(s) == 0:
        return

    # Use a temporary stack to store any numbers, and transfer one number to the temporary stack.
    temp_stack = Stack()
    temp_stack.push(s.pop())

    # While there are still items in the unsorted stack
    while len(s) != 0:
        # Pop one item from the stack, and compare it to the top most item in the temp stack.
        # While the items in the temp stack are bigger, pop them out and push them back to the original stack.
        top = s.pop()
        while len(temp_stack) and top < temp_stack.peek():
            s.push(temp_stack.pop())
        # Then we add the beginning top item to the temp stack.
        temp_stack.push(top)

    # At this point, the items in the temp stack should be arranged in reverse order (biggest on top),
    # so we just pop from the temp stack back to the original stack.
    while len(temp_stack):
        s.push(temp_stack.pop())


if __name__ == '__main__':
    s1 = Stack()
    for i in range(20):
        s1.push(random.randint(1, 99))
    print(s1)
    sort_stack(s1)
    print(s1)
