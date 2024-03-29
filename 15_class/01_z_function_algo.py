# Write a function that takes a string and a pattern
# and returns if the pattern is a substring of the string.
# The function should implement z-function algorithm.
#
# Example
# Input: "abbcdef", "bbcd"
# Output: True


def z_function_algo(string, pattern):
    z = z_func("{}#{}".format(pattern, string))
    for el in z[len(pattern) + 1:]:
        if el == len(pattern):
            return True
    return False


def z_func(string):
    z = [0] * len(string)
    l, r = 0, 0
    for i in range(1, len(string)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(string) and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

# O(S + P) -- time
# O(S + P) -- space
