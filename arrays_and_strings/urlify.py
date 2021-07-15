def urlify(char_array, length):
    """Replace spaces with %20, doing in-place operations."""
    # Solution: O(n) time.

    # We loop through the array from the back.
    # To get the index of the last character from the back, we use the given length.
    r_index = len(char_array) - 1
    l_index = r_index - (len(char_array) - length)
    # We continue to loop until the replacing index is equal to the loop index,
    # which tells us that there is no more space replacements to do.
    while r_index != l_index:
        if char_array[l_index] == ' ':
            char_array[r_index] = '0'
            char_array[r_index-1] = '2'
            char_array[r_index-2] = '%'
            r_index -= 3
        else:
            char_array[r_index] = char_array[l_index]
            r_index -= 1
        l_index -= 1

    return ''.join(char_array)


if __name__ == '__main__':
    print(urlify(list("Mr John Smith    "), 13))
