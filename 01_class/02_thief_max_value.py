#  You are a robber who has found a block of houses to rob.
#  Each house i has a non-negative values[i] worth of value inside that you can steal.
#  However, you can't rob two adjacent houses.
#  What’s the maximum value you can steal from the block?

# As an input you have a non-empty array with non-negative integers.
# Each value under index i is worth of value inside a house at i place.

# Example
# Input: [3, 10, 3, 1, 2]
# Output: 12

def max_val(values):
    a, b = 0, 0
    for val in values:
        a, b = b, max(b, a + val)

    return b

# O(N) -- time
# O(1) -- space
