from itertools import permutations


def permutations_without_dups(s):
    """Calculate all permutations of a string of unique characters."""
    # Base case. If the string is empty, then return.
    if len(s) == 0:
        return {s}

    perms = set()
    # Get the first character
    char = s[0]
    # Remaining string
    remainder = s[1:]
    for p in permutations_without_dups(remainder):
        # Insert a character at every possible location
        for i in range(len(p)+1):
            perms.add("".join(p[:i] + char + p[i:]))
    return perms


if __name__ == '__main__':
    string = "abcd"
    p = permutations_without_dups(string)
    p_i = set("".join(s) for s in permutations(string))
    print(p, p_i)
    print(len(p), len(p_i))

