class MyQueue:
    """This class implements a queue functionality using 2 stacks."""
    def __init__(self):
        # We use stack_one as the main stack to enqueue (push), and stack_two as a temporary stack for de-queueing.
        self.stack_one = []
        self.stack_two = []
        self.last_op_deq = False

    def enqueue(self, data):
        # Solution: O(1) time mostly.
        # Enqueueing is simple where we just add to the end of the relevant stack.

        # We check whether the last operation was a dequeue. If yes, then we move the items back to main stack.
        if self.last_op_deq:
            while len(self.stack_two):
                self.stack_one.append(self.stack_two.pop())
            self.last_op_deq = False

        self.stack_one.append(data)

    def dequeue(self):
        # Solution: O(1) time mostly.
        # Check for length and last operation.
        if (self.last_op_deq and len(self.stack_two) == 0) or (not self.last_op_deq and len(self.stack_one) == 0):
            raise IndexError("no items in queue")

        # If the last operation was not a dequeue, then we move the items to the other stack.
        if not self.last_op_deq:
            # To dequeue, we have to pop everything from the stack and push it into stack_two.
            while len(self.stack_one):
                self.stack_two.append(self.stack_one.pop())
            self.last_op_deq = True

        # Then we return the top element from stack_two, and re-push everything back to stack_one.
        # We do not move the items back in case user dequeues multiple times.
        return self.stack_two.pop()

    def is_empty(self):
        return len(self.stack_one) == 0 if not self.last_op_deq else len(self.stack_two) == 0

    def __str__(self):
        return "One: " + " <- ".join(str(i) for i in self.stack_one) + "\n" + \
               "Two: " + " <- ".join(str(i) for i in self.stack_two)


if __name__ == '__main__':
    queue = MyQueue()
    for i in range(9):
        queue.enqueue(i)
    print(queue)

    for i in range(3):
        print(f"De-queued: {queue.dequeue()}")
        print(queue)

    queue.enqueue(99)
    print(queue)

    while not queue.is_empty():
        print(f"De-queued: {queue.dequeue()}")
        print(queue)
