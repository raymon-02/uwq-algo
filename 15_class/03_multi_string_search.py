# Write a function that takes text and patterns
# and returns if each pattern contains in the text.
#
# Example
# Input: "algorithms are good to know", ["algo", "not", "is", "go", "now"]
# Output: [True, False, False, True, True]

def multi_string_search(text, patterns):
    trie = {}
    for pattern in patterns:
        curr = trie
        for ch in pattern:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["#"] = pattern

    result = set()
    for i in range(len(text)):
        curr = trie
        j = i
        while j < len(text) and text[j] in curr:
            curr = curr[text[j]]
            j += 1
            if "#" in curr:
                result.add(curr["#"])

    return [pattern in result for pattern in patterns]

# O(P * N + T * N) -- time
# O(P * N) -- space

# Note: can be solved by Aho-Corasick algorithm for linear time
