# Write a function that takes a string
# and returns the longest substring without duplicate characters.
#
# Example
# Input: "abcdbafec"
# Output: "cdbafe"


def longest_substring_without_duplication_index(string):
    cache = set()
    l, r = 0, 0
    res_l, res_r = 0, 0

    while r < len(string):
        while string[r] in cache:
            cache.remove(string[l])
            l += 1
        cache.add(string[r])
        r += 1

        if r - l > res_r - res_l:
            res_l, res_r = l, r

    return string[res_l: res_r]


# O(N) -- time
# O(N) -- space


def longest_substring_without_duplication(string):
    cache = {}
    l = 0
    res_l, res_r = 0, 0

    for i, char in enumerate(string):
        if char in cache:
            l = max(l, cache[char])
        cache[char] = i + 1
        if i - l + 1 > res_r - res_l:
            res_l, res_r = l, i + 1

    return string[res_l:res_r]

# O(N) -- time
# O(N) -- space
