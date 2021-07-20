from bit import *


def flip_bit_to_win(n):
    """Find the length of the longest sequence of 1 that we can make by flipping one bit to 1."""
    # Solution: O(b) where b is the number of bits in the number.

    if n == 0:
        print(1)
        return

    max_seq = 1
    curr_seq = 0  # This stores the length of the current sequence where the latest 0 is still 0.
    last_seq = 0  # This stores the length of the last sequence where the latest 0 is flipped.
    while True:
        # If the LSB is 0.
        if (n & 1) == 0:
            max_seq = max(last_seq, max_seq)
            last_seq = curr_seq
            curr_seq = 0
        else:  # If the LSB is 1.
            curr_seq += 1
        last_seq += 1

        if n == 0:
            break
        n = logical_right_shift(n)  # There is no logical right shift.
    # Check for last sequence.
    max_seq = max(max_seq, last_seq)
    print(max_seq)

flip_bit_to_win(int("0b1000", 2))
