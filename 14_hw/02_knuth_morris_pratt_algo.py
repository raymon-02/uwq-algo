# Write a function that takes a string and a pattern
# and returns if the pattern is a substring of the string.
# The function should implement Knuth-Morris-Pratt algorithm.
#
# Example
# Input: "abbcdef", "bbcd"
# Output: True


def knuth_morris_pratt_algo(string, pattern):
    pi = prefix_func("{}#{}".format(pattern, string))
    for el in pi[2 * len(pattern):]:
        if el == len(pattern):
            return True
    return False


def prefix_func(string):
    pi = [0] * len(string)
    for i in range(1, len(string)):
        j = pi[i - 1]
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi

# O(S + P) -- time
# O(S + P) -- space
