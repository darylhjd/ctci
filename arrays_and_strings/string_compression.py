def string_compression(string):
    """Compress a string using counts of repeated letters."""
    # Solution: O(n) time to iterate through string and O(n) auxiliary space to store new string.
    if len(string) == 0:
        return ""

    new_str = []
    curr_letter = string[0]
    counter = 0
    for letter in string:
        if letter == curr_letter:
            counter += 1
            continue
        append_compressed_letter(new_str, curr_letter, counter)
        curr_letter = letter
        counter = 1

    # We need this so the last letter is also appended
    append_compressed_letter(new_str, curr_letter, counter)
    return min(string, ''.join(new_str), key=len)


def append_compressed_letter(char_array: list, letter, count):
    char_array.append(letter)
    while count != 0:
        char_array.append(str(count % 10))
        count //= 10
