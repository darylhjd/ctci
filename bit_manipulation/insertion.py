def insertion(n, m, j, i):
    # First we have to clear the j - i bits in n.

    print(bin(n))
    for shift in range(j, i, -1):
        n &= ~(1 << shift)
    print(bin(n))

    # Move m i bits to the left
    m <<= i
    print(bin(n | m))

insertion(2**10, 2**4 + 2**1 + 1, 6, 2)
