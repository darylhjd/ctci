import math


def rotate_matrix(m):
    """Rotate a NxN matrix 90 degrees inplace."""
    # Solution: 0(n^2) time to go through each matrix element.

    # Assume rotating clockwise
    # Do sanity checks for the matrix
    if len(m) == 0 or len(m[0]) == 0:  # If row or column is empty.
        return
    elif len(m) != len(m[0]):  # If wrong dimensions
        return

    aux = None  # Use this to store the temporary variable
    start = 0
    end = len(m[0]) - 1
    rotation = 0
    while rotation < math.ceil(len(m[0]) / 2):
        replacement = 0
        while start + rotation < end - rotation - replacement:
            # Store the auxiliary (upper left)
            aux = m[start+rotation][end-rotation-replacement]
            # Replace upper right with upper left
            m[start+rotation][end-rotation-replacement] = m[start+rotation+replacement][start+rotation]
            # Replace upper left with lower left
            m[start+rotation+replacement][start+rotation] = m[end-rotation][start+rotation+replacement]
            # Replace lower left with lower right
            m[end-rotation][start+rotation+replacement] = m[end-rotation-replacement][end-rotation]
            # Replace lower right with aux
            m[end-rotation-replacement][end-rotation] = aux
            replacement += 1
        rotation += 1
