def parens(n):
    """Print all valid combinations of n pairs of parentheses (properly opened and closed)."""
    stack = []
    return helper(n, 0, 0, stack)


def helper(n, balance, total, stack):
    # Termination case.
    # If the pairs of parentheses is equal to n, then print this combination.
    if total == n:
        print("".join(stack))
        return

    # There are a few cases to consider.
    # 1. If balance + total = n, then we can only close.
    if balance + total == n:
        stack.append(")")
        helper(n, balance-1, total+1, stack)
        stack.pop()
    # 2. If balance + total < n, then there are two inner cases to consider.
    elif balance + total < n:
        # If 0 <= balance < n, then we can add another opening.
        # Notice that we leave out the balance == n case since we will not be able to add another opening
        # if that were the case.
        if 0 <= balance < n:
            stack.append("(")
            helper(n, balance+1, total, stack)
            stack.pop()
        # 2. If 0 < balance<= n, then we can add another closing.
        # Notice that we leave out the balance == 0 case since we will not be able to add another closing
        # if that were the case.
        if 0 < balance <= n:
            stack.append(")")
            helper(n, balance-1, total+1, stack)
            stack.pop()


if __name__ == '__main__':
    parens(5)
