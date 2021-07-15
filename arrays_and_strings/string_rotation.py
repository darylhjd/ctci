def string_rotation(str1, str2):
    """Check if one string is a rotation of another."""
    # Solution: O(n^2) time for iterating through each starting point and checking through.

    # Check if same length
    if len(str1) != len(str2):
        return False

    checks = 0
    while checks < len(str1):
        is_substring = True
        # For every iteration through
        for s1_index in range(len(str1)):
            s2_index = (checks + s1_index) % len(str1)
            if str1[s1_index] != str2[s2_index]:
                is_substring = False
                break

        if is_substring:
            return True
        checks += 1
    return False
