# Write a function that takes a string
# and returns the longest palindrome
# containing in the string.
# The function should use hash method.
#
# Example
# Input: "abbacacabc"
# Output: "bacacab"


def longest_palindrome_hash(string):
    powers = [1] * len(string)
    p = 31
    for i in range(1, len(string)):
        powers[i] = powers[i - 1] * p

    hashes = [0] * len(string)
    hashes[0] = ord(string[0]) - ord('a') + 1
    for i in range(1, len(string)):
        hashes[i] = (ord(string[i]) - ord('a') + 1) * powers[i]
        hashes[i] += hashes[i - 1]
    rev_hashes = [0] * len(string)
    rev_hashes[-1] = ord(string[-1]) - ord('a') + 1
    for i in range(1, len(string)):
        j = len(string) - i - 1
        rev_hashes[j] = (ord(string[j]) - ord('a') + 1) * powers[i]
        rev_hashes[j] += rev_hashes[j + 1]

    result = string[0]

    # odd length
    for i in range(1, len(string) - 1):
        l, r = 1, min(i, len(string) - i - 1) + 1
        while l < r:
            m = l + (r - l) // 2
            i1, i2 = i - m, i + m
            hash1 = hashes[i]
            hash1 -= hashes[i1 - 1] if i1 > 0 else 0
            hash2 = rev_hashes[i]
            hash2 -= rev_hashes[i2 + 1] if i2 + 1 < len(string) else 0
            j2 = len(string) - i2 - 1
            comp1 = i1 <= j2 and hash1 * powers[j2 - i1] == hash2
            comp2 = j2 <= i1 and hash2 * powers[i1 - j2] == hash1
            if comp1 or comp2:
                s = string[i1:i2 + 1]
                result = result if len(s) < len(result) else s
                l, r = m + 1, r
            else:
                l, r = l, m

    # even length
    for i in range(0, len(string) - 1):
        l, r = 0, min(i, len(string) - i - 2) + 1
        while l < r:
            m = l + (r - l) // 2
            i1, i2 = i - m, i + 1 + m
            hash1 = hashes[i]
            hash1 -= hashes[i1 - 1] if i1 > 0 else 0
            hash2 = rev_hashes[i + 1]
            hash2 -= rev_hashes[i2 + 1] if i2 + 1 < len(string) else 0
            j2 = len(string) - i2 - 1
            comp1 = i1 <= j2 and hash1 * powers[j2 - i1] == hash2
            comp2 = j2 <= i1 and hash2 * powers[i1 - j2] == hash1
            if comp1 or comp2:
                s = string[i1:i2 + 1]
                result = result if len(s) < len(result) else s
                l, r = m + 1, r
            else:
                l, r = l, m

    return result

# O(NlogN) -- time
# O(N) -- space
