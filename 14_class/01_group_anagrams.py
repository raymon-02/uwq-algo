# Write a function that takes array of string
# and returns groups of anagrams based on these strings.
# Strings consist of 'a'..'z' letters only.
#
# Example
# Input: ["abc", "yz", "zy", "cba", "aaa", "cbdd", "bcdd"]
# Output: [["aaa"], ["yz", "zy"], ["abc", "cba"], ["cbdd", "bcdd"]]


from collections import defaultdict


def group_anagrams(words):
    powers = [1] * 26
    p = 31
    for i in range(1, 26):
        powers[i] = powers[i - 1] * p

    groups = defaultdict(list)
    for word in words:
        word_hash = 0
        for ch in word:
            word_hash += powers[ord(ch) - ord('a')]
        groups[word_hash].append(word)

    return list(groups.values())

# O(W * N) -- time
# O(W * N) -- space
