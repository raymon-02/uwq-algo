# Write a function that takes sorted array of distinct integers
# and returns the first index in the array
# that equals to the value at that index.
# If there is no such index the function should return -1.
#
# Example
# Input: [-2, -1, 0, 3, 4, 5, 8]
# Output: 3


def index_equals_value(arr):
    def rec(l, r):
        if l >= r:
            return -1

        m = (l + r) // 2

        if m <= arr[m]:
            result = rec(l, m)
        else:
            result = rec(m + 1, r)

        if arr[m] == m and (result == -1 or m < result):
            result = m

        return result

    return rec(0, len(arr))

# O(logN) -- time
# O(logN) -- space
