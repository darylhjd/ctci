def convert(a, b):
    """Determine the number of bits to flip to convert A to B."""

    # How do we figure out which bits are different?
    # To do that, we do a XOR operation on both numbers.
    # The result is a number whose bits which are 1 indicate different bits.
    temp = a ^ b

    # Then we can count the number of bits which are 1.
    # We could use a logical shift right and keep counting the LSB. 
    # But that is annoying since Python does not have a logical shift,
    # so we can come up with a different method.
    # What we can do is to c & (c-1) together.
    # Subtracting will flip the right-most 1 to 0 and & will give a non-zero result if 
    # there are still any 1s in the number.
    # This is the same as counting how many 1 bits are in the number.
    count = 0
    while temp != 0:
        count += 1
        temp = temp & (temp - 1)
    print(count)