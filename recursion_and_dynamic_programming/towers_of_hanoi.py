def towers_of_hanoi(N, start, aux, end):
    """Use stacks."""
    # Base case. If N is 0, no disks to move.
    if N == 0:
        return

    # Move N-1 disks to aux.
    towers_of_hanoi(N-1, start, end, aux)
    # Move the last N disk to end
    end.append(start.pop())
    # Then we move the remaining N-1 disks to the end from the aux.
    towers_of_hanoi(N-1, aux, start, end)


if __name__ == '__main__':
    n = 22
    s = [i for i in range(n, 0, -1)]
    a = []
    e = []
    towers_of_hanoi(n, s, a, e)
    print(e)
