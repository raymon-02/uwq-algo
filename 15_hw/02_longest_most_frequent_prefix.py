# Write a function that takes unique strings
# and returns the most frequent prefix
# that appears in these strings.
# If there are two or more such prefixes
# the function should return the longest one.
#
# Example
# Input: ["algo", "alloc", "alu", "cat", "catana"]
# Output: "al"
#
# Example
# Input: ["abcd", "efg", "hi"]
# Output: "abcd"


class Node:
    def __init__(self):
        self.nodes = {}
        self.count = 0


def longest_most_frequent_prefix(strings):
    result, ri, count = "", 0, 0

    trie = Node()
    for string in strings:
        curr = trie
        for i, ch in enumerate(string):
            if ch not in curr.nodes:
                curr.nodes[ch] = Node()
            curr.nodes[ch].count += 1

            if curr.nodes[ch].count > count or curr.nodes[ch].count == count and i + 1 > ri:
                result, ri, count = string, i + 1, curr.nodes[ch].count

            curr = curr.nodes[ch]

    return result[:ri]

# (S * N) -- time
# (S * N) -- space
