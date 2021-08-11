def helper(a, b):
    smaller = a if a < b else b
    bigger = a if smaller == b else b
    return recursive_multiply(smaller, bigger)


def recursive_multiply(a, b):
    """Write a recursive function to multiply two positive integers without using
    the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
    minimize the number of those operations."""
    if b == 0 or a == 0:
        return 0
    elif a == 1:
        return b

    # Let a be the multiplier and b be the multiplied.
    # We divide a by 2.
    mult = a >> 1
    res = recursive_multiply(mult, b)
    if a % 2 == 0:
        return res + res
    else:
        return res + res + b


if __name__ == '__main__':
    print(helper(999, 999))
