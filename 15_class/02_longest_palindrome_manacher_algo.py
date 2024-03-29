# Write a function that takes a string
# and returns the longest palindrome
# containing in the string.
# The function should use Manacher algorithm.
#
# Example
# Input: "abbacacabc"
# Output: "bacacab"


def longest_palindrome_manacher_algo(string):
    l, r = 0, -1
    d1 = [0] * len(string)
    for i in range(len(string)):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < len(string) and string[i - k] == string[i + k]:
            k += 1
        d1[i] = k
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

    l, r = 0, -1
    d2 = [0] * len(string)
    for i in range(len(string)):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < len(string) and string[i - k - 1] == string[i + k]:
            k += 1
        d2[i] = k
        if i + k - 1 > r:
            l = i - k
            r = i + k - 1

    d, result = 0, ""
    for i, k in enumerate(d1):
        if 2 * k - 1 > d:
            d, result = 2 * k - 1, string[i - k + 1: i + k]
    for i, k in enumerate(d2):
        if 2 * k > d:
            d, result = 2 * k, string[i - k: i + k]

    return result

# O(N) -- time
# O(N) -- space
