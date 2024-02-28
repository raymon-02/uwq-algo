# Write a function that takes prices of juice
# and returns the indices of prices from which
# the maximum profit can be constructed.
# Each price under index i represents i amount of juice
# and the maximum amount of juice is n - 1
# where n is a length of prices.
#
# Each amount of juice can be used multiple times.
#
# At index 0 in prices there will be always 0 value
# as price for 0 amount of juice is 0.
#
# Example
# Input: [0, 1, 3, 2]
# Output: [1, 2]
# The maximum amount of juice is 3 as length of prices is 4.
# 1 amount of juice has price 1.
# 2 amount of juice has price 3.
# In sum it is 1+2=3 amount of juice with profit 1+3=4.
# This is the maximum profit that can be constructed
# having 3 amount of juice in total.
#
# Example
# Input: [0, 2, 3]
# Output: [1, 1]
# The maximum amount of juice is 2 as length of prices is 3.
# 1 amount of juice has price 2.
# We can use 1 amount of juice multiple times.
# In sum it is 1+1=2 amount of juice with profit 2+2=4.
# This is the maximum profit that can be constructed
# having 2 amount of juice in total.


def juice_grid(prices):
    n = len(prices)
    grid = [[0] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            take = grid[i - j][j] + prices[j] if i - j >= 0 else 0
            leave = grid[i][j - 1]
            grid[i][j] = max(take, leave)

    result = []
    i, j = n - 1, n - 1
    while j > 0 and i > 0:
        if grid[i][j] == grid[i][j - 1]:
            j -= 1
        else:
            result.append(j)
            i -= j

    return list(reversed(result))


# O(N^2) -- time
# O(N^2) -- space

# No need to have full grid.


def juice(prices):
    n = len(prices)
    grid = [0] * n
    path = [0] * n
    for j in range(1, n):
        for i in range(j, n):
            if grid[i - j] + prices[j] > grid[i]:
                grid[i] = grid[i - j] + prices[j]
                path[i] = j

    result = []
    i = n - 1
    while i > 0:
        result.append(path[i])
        i -= path[i]

    return list(reversed(result))

# O(N^2) -- time
# O(N) -- space
