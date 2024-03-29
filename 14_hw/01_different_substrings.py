# Write a function that takes a string
# and returns the number of different substring in the string.
#
# Example
# Input: "abbabba"
# Output: 17

from collections import Counter


def different_substrings(string):
    powers = [1] * len(string)
    p = 31
    for i in range(1, len(string)):
        powers[i] = powers[i - 1] * p

    hashes = [0] * len(string)
    hashes[0] = ord(string[0]) - ord('a') + 1
    for i in range(1, len(string)):
        hashes[i] = (ord(string[i]) - ord('a') + 1) * powers[i]
        hashes[i] += hashes[i - 1]

    result = 0
    for length in range(1, len(string) + 1):
        groups = Counter()
        for i in range(len(string) - length + 1):
            current_hash = hashes[i + length - 1]
            current_hash -= hashes[i - 1] if i > 0 else 0
            current_hash *= powers[len(string) - i - 1]
            groups[current_hash] += 1
        result += groups.total()

    return result

# O(N^2) -- time
# O(N) -- space
