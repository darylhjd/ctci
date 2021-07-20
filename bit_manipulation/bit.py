def logical_right_shift(n):
    return (n >> 1) if n >= 0 else ((n + (1 >> (n.bit_length() - 1))) >> 1)
