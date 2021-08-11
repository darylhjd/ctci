def robot_in_a_grid(c_col, c_row, r, c, path: list, limits, failed):
    """A robot is sitting on the upper left corner of grid with r rows and c columns.
    Find a path from the upper left to the bottom right, while avoiding off limit cells.

    Assume that rows and columns are zero-indexed."""
    # Base case. If the robot is at the bottom right, then return the path.
    if c_col == c and c_row == r:
        path.append((c_col, c_row))
        return True
    elif c_col > c or c_row > r:
        return False

    # Check if this position is off limits or it is in failed paths already.
    if (c_col, c_row) in limits or (c_col, c_row) in failed:
        return False

    # Append this position to the path.
    path.append((c_col, c_row))

    # We can move either down or to the right.
    # Try moving down first.
    down_result = robot_in_a_grid(c_col, c_row + 1, r, c, path, limits, failed)
    if down_result:  # If we can move down, then return True.
        return True

    # If cannot move down, try moving to the right.
    right_result = robot_in_a_grid(c_col + 1, c_row, r, c, path, limits, failed)
    if right_result:  # Similarly, if we can move right, return True.
        return True

    # If we reach here, means both options not viable.
    # Remove current position from the path and add it to failed paths.
    failed.add(path.pop())
    return False


if __name__ == '__main__':
    path = []
    limits = set()
    for r in range(1, 4):
        for c in range(2, 4):
            limits.add((c, r))

    block = False
    if block:
        limits.add((4, 1))
        limits.add((1, 4))
    failed = set()
    print(robot_in_a_grid(0, 0, 4, 4, path, limits, failed), path)
