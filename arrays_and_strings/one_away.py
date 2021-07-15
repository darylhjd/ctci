def one_away(str1, str2):
    """Check if the strings are one edit away from being similar.
    This can involve inserting, removing or changing a letter from a string."""
    # Solution: O(n) time, where n is the length of the longer string.

    # Check the string lengths.
    # If the length has difference of more than 1, more than 1 insertion/removal required.
    if abs(len(str1) - len(str2)) > 1:
        return False
    # If the length has no difference, check for letter replacement.
    elif len(str1) - len(str2) == 0:
        has_change = False
        for one_c, two_c in zip(str1, str2):
            if one_c != two_c and has_change:
                return False
            elif one_c != two_c:
                has_change = True
    # If the length has difference of one, we can reduce problem to check letter insertion.
    else:
        shorter = str1 if len(str1) < len(str2) else str2
        longer = str1 if shorter == str2 else str2
        s_index = l_index = 0
        has_change = False
        while s_index < len(shorter):
            s_char = shorter[s_index]
            l_char = longer[l_index]
            if s_char != l_char and has_change:
                return False
            elif s_char != l_char:
                has_change = True
                l_index += 1
            else:
                l_index += 1
                s_index += 1
    return True
