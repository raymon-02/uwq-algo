# Write a function that takes two strings
# and returns the smallest substring of the first string
# which contains all chars from the second substring.
# If there is no such substring then function should return None.
#
# Example
# Input: "abaefc$be$adc", "abc$$"
# Output: "c$be$a"


from collections import Counter


def smallest_substring_containing(string, chars):
    initial = Counter(chars)
    current = Counter()
    curr = 0
    found = False
    res_l, res_r = 0, len(string)
    l, r = 0, 0

    while r < len(string):
        while curr != len(chars) and r < len(string):
            current[string[r]] += 1
            if current[string[r]] <= initial[string[r]]:
                curr += 1
            r += 1
        if curr != len(chars):
            break
        found = True
        while curr == len(chars):
            current[string[l]] -= 1
            if current[string[l]] < initial[string[l]]:
                curr -= 1
            l += 1
        if r - l + 1 < res_r - res_l:
            res_l, res_r = l - 1, r

    if not found:
        return None

    return string[res_l:res_r]

# O(S + C) -- time
# O(S + C) -- space
