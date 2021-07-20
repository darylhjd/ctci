from bit import *


def next_number(n):
    """Given a positive number, print the next smallest and next largest number that have the
    same number of 1 bits in their binary representation."""
    # Get the numbers of 1s in the current number.
    ones = 0
    while n != 0:
        if (n & 1) == 1:
            ones += 1
        n = logical_right_shift(n)
    
    # To get the smallest number