from collections import Counter


def counter_solution(s1, s2):
    """Uses a counter to check the frequency of each character appearing."""
    if len(s1) != len(s2):
        return False

    # Solution: O(n) time and O(n) auxiliary space
    one_counter = Counter(s1)
    two_counter = Counter(s2)
    return one_counter == two_counter


def sort_solution(s1, s2):
    """Sorts and then compares to see if the strings are the same"""
    if len(s1) != len(s2):
        return False

    # Solution: O(nlogn) time for the sorting.
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
