class MinStack:
    """This class also keeps track of the minimum value in an array in O(1) time.
    Like any other stack, Push, Pop operations are also done in O(1) time."""
    def __init__(self):
        # It is important to realise that there is no way of implementing the min function
        # without the use of additional space.
        # What we can then do is to use another stack to keep track of the minimum nodes as they are added.
        # If a minimum node is removed, it is popped from the stack keeping track of the minimums.
        self.minimums = []
        self.stack = []

    def push(self, data):
        """Push a value onto the stack"""
        if len(self.minimums) == 0 or self.minimums[-1] >= data:
            self.minimums.append(data)
        self.stack.append(data)

    def pop(self):
        to_pop = self.stack.pop()
        if self.minimums[-1] == to_pop:
            self.minimums.pop()
        return to_pop

    def min(self):
        return self.minimums[-1]


# We can also use a form where the nodes of the stack know what the minimum of the stack below is and including it.
# Then, we can just get the value of the min field of the Node. However, this will take up more space than the solution
# above since every node will need to store extra information.
