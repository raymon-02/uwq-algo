# There is an array of positive integers
# where each integer represents the maximum number of steps
# you can take forward in the array.
# If the element is 3 then you can take 1, 2 or 3 steps.
#
# Write a function that takes such array
# and returns the minimum number of jumps needed
# to reach the last index of the array.
#
# Example
# Input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 3]
# Output: 4
# Index 0, take 1 step  => 1 jump
# Index 1, take 4 steps => 1 jump
# Index 5, take 1 step  => 1 jump
# Index 6, take 4 steps => 1 jump
# All is 4 jumps


def min_jumps_grid(arr):
    result = [float("inf")] * len(arr)
    result[0] = 0

    for i, max_step in enumerate(arr):
        for j in range(i + 1, min(len(arr), i + max_step + 1)):
            result[j] = min(result[j], result[i] + 1)

    return result[-1]


# O(N^2) -- time
# O(N) -- space

# No need to save results.


def min_jumps(arr):
    if len(arr) <= 1:
        return 0

    max_reach = arr[0]
    steps = arr[0]
    result = 0

    for i, max_step in enumerate(arr[1:-1]):
        max_reach = max(max_reach, i + max_step)
        steps -= 1
        if steps == 0:
            result += 1
            steps = max_reach - i

    return result + 1

# O(N) -- time
# O(1) -- space
