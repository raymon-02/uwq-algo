# Write a function that takes unique strings
# and returns the shortest unique prefix for each string.
# The shortest unique prefix of the string means
# the prefix which identifies the string uniquely.
# If a string is a prefix of another string entirely
# then the shortest unique prefix for the first string
# is the whole string itself.
#
# Example
# Input: ["hello", "hel", "abra", "abba", "axel"]
# Output: ["hell", "hel", "abr", "abb", "ax"]


class Node:
    def __init__(self):
        self.nodes = {}
        self.count = 0


def shortest_unique_prefix(strings):
    trie = Node()
    for string in strings:
        curr = trie
        for ch in string:
            if ch not in curr.nodes:
                curr.nodes[ch] = Node()
            curr.nodes[ch].count += 1
            curr = curr.nodes[ch]
        curr.nodes["#"] = string

    result = []
    for string in strings:
        prev = trie
        for i, ch in enumerate(string):
            curr = prev.nodes[ch]
            if curr.count == 1 or curr.nodes.get("#", None) == string:
                result.append(string[:i + 1])
                break

    return result

# O(S * N) -- time
# O(S * N) -- space
