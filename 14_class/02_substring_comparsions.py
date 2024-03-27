# There is a string.
# Write a function that takes this string and list of triples
# where each triple represents length and two start indices
# for substrings of the input string.
# The function should return if two substrings are equal with each other
# for each triple.
#
# Example
# Input: "abcdababcd", [(4, 0, 6), (3, 0, 4)]
# Output: [True, False]
# The first triple represents substrings with length 4:
#     the first substring starts at index 0:  "abcd"
#     the second substring starts at index 6: "abcd"
# The second triple represents substrings with length 3:
#     the first substring starts at index 0:  "abc"
#     the second substring starts at index 6: "aba"


def substring_comparisons(string, triples):
    powers = [1] * len(string)
    p = 31
    for i in range(1, len(string)):
        powers[i] = powers[i - 1] * p

    hashes = [0] * len(string)
    hashes[0] = ord(string[0]) - ord('a') + 1
    for i in range(1, len(string)):
        hashes[i] = (ord(string[i]) - ord('a') + 1) * powers[i]
        hashes[i] += hashes[i - 1]

    result = []
    for (length, i1, i2) in triples:
        if i1 == i2:
            result.append(True)
            continue
        hash1 = hashes[i1 + length - 1]
        hash1 -= hashes[i1 - 1] if i1 > 0 else 0
        hash2 = hashes[i2 + length - 1]
        hash2 -= hashes[i2 - 1] if i2 > 0 else 0
        comp1 = i1 < i2 and hash1 * powers[i2 - i1] == hash2
        comp2 = i2 < i1 and hash2 * powers[i1 - i2] == hash1
        result.append(comp1 or comp2)

    return result

# O(S + T) -- time
# O(S + T) -- space
