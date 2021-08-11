def power_set(s: set, p_set: set):
    """Return all subsets of a set."""
    # Check if this set is alreay in the power set
    if s in p_set:
        return

    # Add current set to the power_set
    p_set.add(frozenset(s))

    # Create a list from the set so we can loop over
    s_list = list(s)
    for v in s_list:
        # Remove current value from the set
        s.discard(v)
        # then repeat the process
        power_set(s, p_set)
        # Add the element back to the set
        s.add(v)


if __name__ == '__main__':
    p = set()
    se = {i for i in range(3)}
    power_set(se, p)
    assert len(p) == 2 ** len(se)
    print([set(s) for s in p])
