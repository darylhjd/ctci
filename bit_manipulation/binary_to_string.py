def binary_to_string(double: float):
    """Given a real number betwen 0 and 1, print the binary representation of the number.
    If the number cannot be accurately represented between 32 characters, print error."""

    characters = 0
    string_rep = "0."
    while characters < 32:
        double *= 2
        if double >= 1:
            string_rep += "1"
            double -= 1
        else:
            string_rep += "0"
        if double.is_integer():
            print(string_rep)
            return
        characters += 1
    print("ERROR")


binary_to_string(0.656785)