from collections import defaultdict


def palindrome_permutation(string: str):
    """Check if the given string is a permutation of a palindrome."""
    # Solution: O(n) time for creating the counter, and O(n) auxiliary space (worst case each letter is different),
    # where n is the length of the string.

    # We use the property of a palindrome that for even length strings,
    # all letters will occur an even number of times, while for a odd length string,
    # there can only be one letter that occurs an odd number of times.

    # Sanitise string
    string = ''.join(string.lower().replace(" ", ""))
    counter = defaultdict(int)
    for letter in string:
        counter[letter] += 1

    if len(string) % 2:
        has_odd = False
        for letter, count in counter.items():
            if count % 2 and has_odd:
                return False
            elif count % 2:
                has_odd = True
    else:
        for letter, count in counter.items():
            if count % 2:
                return False
    return True
