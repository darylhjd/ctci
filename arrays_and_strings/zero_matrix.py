def zero_matrix_hash_set(m):
    """Make the entire row and column in which a zero appears all 0."""
    # Solution: O(n^2) time to go through each element in the matrix, O(n) space to store zero-indexes.

    # Check for invalid matrices
    if len(m) == 0 or len(m[0]) == 0:
        return

    # Store any indexes which have a zero
    zero_rows = set()
    zero_cols = set()

    for row_index in range(len(m)):
        for col_index in range(len(m[0])):
            if m[row_index][col_index] == 0:
                zero_rows.add(row_index)
                zero_cols.add(col_index)

    # Do replacements
    for row in zero_rows:
        for col in range(len(m[0])):
            m[row][col] = 0
    for col in zero_cols:
        for row in range(len(m)):
            m[row][col] = 0


def zero_matrix_no_space(m):
    """Make entire row and column in which a zero appears all 0, but with no additional space requirement."""
    # Solution: O(n^2) time to go through each element. O(1) auxiliary space.

    # Check for invalid matrices
    if len(m) == 0 or len(m[0]) == 0:
        return

    # The trick to this method is to store whether a row or column is to be zero-ed in the first row/column.
    # To do this, we must first check whether the first row/column has zeros themselves.
    row_has_zero = col_has_zero = False
    for col in m[0]:
        if col == 0:
            row_has_zero = True
    for row in range(len(m)):
        if m[row][0] == 0:
            col_has_zero = True

    # Then, we loop through the rest of the matrix.
    # However, this time, when we meet a element that is zero,
    # we store that we have met a zero in the corresponding first row/column.
    for row in range(1, len(m)):
        for col in range(1, len(m[0])):
            if m[row][col] == 0:
                # We set the "headers" to zero.
                m[0][col] = 0
                m[row][0] = 0

    # Then, we loop through the first row/col, and then see which col/row is to be zero-ed.
    for col in range(1, len(m[0])):
        if m[0][col] == 0:
            for row in range(1, len(m)):
                m[row][col] = 0

    for row in range(1, len(m)):
        if m[row][0] == 0:
            for col in range(1, len(m[0])):
                m[row][col] = 0

    # Then, we can zero the first row/col based on the values from the first pass
    if row_has_zero:
        for col in range(len(m[0])):
            m[0][col] = 0
    if col_has_zero:
        for row in range(len(m)):
            m[row][0] = 0