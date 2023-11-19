# Write a function that takes a non-empty array of integers
# and returns the maximum sum that can be constructed
# by summing up all the integers in a non-empty subarray of the input array.
# A subarray must only contain adjacent numbers.
#
# Example
# Input: [1, 4, -10, 2, 3]
# Output: 5
# Subarray will be [1, 4]

def kadanes_algo(arr):
    result = float("-inf")
    current = float("-inf")
    for el in arr:
        current = max(current + el, el)
        result = max(result, current)
    return result

# O(N) -- time
# O(1) -- space
