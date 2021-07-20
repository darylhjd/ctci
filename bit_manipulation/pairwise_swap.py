from bit import *


def pairwise_swap(n):
    """Perform a pairwise swap for odd-even bits in the number with as few instructions as possible.
    eg. swap 0 and 1, 2 and 3, etc..."""

    mask = 0
    for i in range(0, 64, 2):
        mask += 2 ** i
    
    # Odd numbers
    odds = mask & n
    # Even numbers
    evens = (mask << 1) & n

    # Do swap
    swap = logical_right_shift(evens) | odds << 1
    print(swap)


pairwise_swap(477)