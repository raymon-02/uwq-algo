# There is an array `items` where each element
# is an array of two positive integers.
# The first integer represents value.
# The second integer represents weight.
#
# Write a function that takes the array and positive integer
# representing a capacity of backpack
# and returns the maximum value
# that can be constructed from values of `items`
# and indices of taken items
# if weights of taken items is not more than backpack capacity.
#
# Example
# Input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
# Output: [10, [1, 3]]
# The maximum 10 value can be constructed from items
# under indices 1 and 3: 4 + 6 = 10.
# The weights of these items is not more than 10: 3 + 7 = 10


def backpack(items, capacity):
    items.insert(0, [0, 0])
    grid = [[0] * len(items) for _ in range(capacity + 1)]
    for i in range(1, capacity + 1):
        for j in range(1, len(items)):
            take = grid[i - items[j][1]][j - 1] + items[j][0] if i - items[j][1] >= 0 else 0
            leave = grid[i][j - 1]
            grid[i][j] = max(take, leave)

    i, j = capacity, len(items) - 1
    path = []
    while j > 0:
        if grid[i][j] == grid[i][j - 1]:
            j -= 1
        else:
            path.append(j - 1)
            i -= items[j][1]
            j -= 1

    return [grid[-1][-1], list(reversed(path))]

# O(N * M) -- time
# O(N * M) -- space
