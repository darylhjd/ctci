def triple_step(n):
    """Calculate the number of ways a person can climb to the nth step if he can take
    either 1, 2, or 3 steps at one go."""
    # Solution: ?

    # Let F(n) be the number of steps that a person can take to go to the nth step.
    # The person can first go to the n-1 step then take 1 step forward,
    # or go to the n-2 step then take 2 steps forward,
    # or to the n-3 step and take 3 steps forward.
    # In each case, we can then simplify the problem to this recurrence relation:
    # F(n) = F(n-1) + F(n-2) + F(n-3)

    # We will be able to calculate this iteratively.
    if n < 0:
        return 0
    elif n <= 2:
        return n

    a = 1
    b = 1
    c = 2
    for i in range(2, n):
        a, b, c = b, c, a + b + c
    return c


if __name__ == '__main__':
    print(triple_step(3))
