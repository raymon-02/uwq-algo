# Write a function that takes a string and a pattern
# and returns if the pattern is a substring of the string.
# The function should implement Rabin-Karp algorithm.
#
# Example
# Input: "abbcdef", "bbcd"
# Output: True


def rabin_karp_algo(string, pattern):
    powers = [1] * max(len(string), len(pattern))
    p = 31
    for i in range(1, len(powers)):
        powers[i] = powers[i - 1] * p

    hashes = [0] * len(string)
    hashes[0] = ord(string[0]) - ord('a') + 1
    for i in range(1, len(string)):
        hashes[i] = (ord(string[i]) - ord('a') + 1) * powers[i]
        hashes[i] += hashes[i - 1]

    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash += (ord(pattern[i]) - ord('a') + 1) * powers[i]

    for i in range(len(string) - len(pattern) + 1):
        current_hash = hashes[i + len(pattern) - 1]
        current_hash -= hashes[i - 1] if i > 0 else 0
        if current_hash == pattern_hash * powers[i]:
            return True

    return False

# O(S + P) -- time
# O(S + P) -- space
