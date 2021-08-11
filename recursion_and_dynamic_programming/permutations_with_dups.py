from collections import Counter


def permutations_with_dups(s):
    # Calculate a hash table of all the frequencies of each letter
    counts = Counter(s)
    return helper(counts)


def helper(counts: Counter):
    perms = set()
    all_zero = True
    for character in counts:
        if counts[character] <= 0:
            continue
        all_zero = False

        counts.subtract(character)
        for perm in helper(counts):
            perms.add(character + perm)
        counts[character] += 1
    if all_zero:
        return {""}
    return perms


if __name__ == '__main__':
    print(len(permutations_with_dups("abcd")))
