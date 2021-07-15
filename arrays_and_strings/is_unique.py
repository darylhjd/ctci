def using_set(string):
    """Use a set to store visited letters"""
    # Solution: O(n) time and O(n) auxiliary space.
    visited = set()
    for letter in string:
        if letter in visited:
            return False
        visited.add(letter)
    return True


def no_ds_brute_force(string):
    """Brute force solution"""
    # Solution: O(n^2) time.
    for index, c_one in enumerate(string):
        for c_two in string[index + 1:]:
            if c_one == c_two:
                return False
    return True


def no_ds_bit_vector(string):
    """Using bits to store the occurrence of a character"""
    # Solution: O(n) time and O(1) auxiliary space.
    # This integer has at least 32bits depending on the machine.
    # We assume that only a-z characters are present.
    b = 0
    for c in string:
        if (b >> ord(c)) & 1:
            return False
        b |= 1 << ord(c)
    return True