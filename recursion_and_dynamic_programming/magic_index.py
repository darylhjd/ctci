def magic_index(A):
    """Given a sorted array of distinct integers, find a magic index if one exists."""
    # Solution: O(logn)

    # We could do a modified binary search.
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = ((high - low) // 2) + low
        if A[mid] == mid:
            return mid
        elif A[mid] > mid:  # If the integer is more than the index, then we search below.
            high = mid - 1
        else:
            low = mid + 1
    return -1  # There is no magic index.


def magic_index_non_distinct(A, low, high):
    """Find a magic index. However, while the integers are sorted, they may not be unique."""

    # If the numbers are non-distinct, then we cannot assume that the magic number will either
    # be below or above the current index.
    # Therefore we will still have to continue to search.
    # However, we need only search from an index that is less than or equal (left side) or more than or equal (right
    # side).
    if low > high:
        return -1

    # Calculating mid
    mid = ((high - low) // 2) + low
    # Check for mid conditions
    if A[mid] == mid:
        return mid
    elif A[mid] < mid:
        high = min(mid-1, A[mid])
        return magic_index_non_distinct(A, low, high)
    else:
        low = max(mid+1, A[mid])
        return magic_index_non_distinct(A, low, high)


if __name__ == '__main__':
    print(magic_index([1, 2, 4, 5, 6, 9, 10]))
    print(magic_index([-3, 0, 2, 5, 6, 7, 8]))