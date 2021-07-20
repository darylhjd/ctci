def draw_line(byte_array, width, x1, x2, y):
    # Assume that x and y are 0-indexed.

    fbi = y * (width // 8) + (x1 // 8)  # Find the index of the first byte where change expected
    lbi = y * (width // 8) + (x2 // 8)  # Find the index of the last byte where change expected

    # Set middle arrays
    for i in range(fbi + 1, lbi):
        byte_array[i] = 0xFF

    # Based on logical left shifting.
    start_offset = x1 % 8
    end_offset = 8 - (x2 % 8 + 1)
    if fbi == lbi:  # If all changes happen within 1 array
        # We combine the masking
        byte_array[fbi] |= ~(~0 << start_offset) & (~0 << end_offset)
    else:
        # Set the first array
        byte_array[fbi] = ~(~0 << start_offset)
        # Set the last array
        byte_array[lbi] = ~0 << end_offset