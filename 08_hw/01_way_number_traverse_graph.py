# Write a function that takes two positive integers
# and returns the number of ways from the top left corner
# to reach the bottom right corner
# in the grid-shaped rectangular graph
# with width and height of the input integers.
#
# Example
# Input: 2, 3
# Output: 3
# Graph:
#  _ _ _
# |_|_|_|
# |_|_|_|
# Possible ways:
# 1. right, right, down
# 2. right, down, right
# 3. down, right, right
# Total ways = 3


def rec_graph_grid(n, m):
    grid = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]


# O(N * M) -- time
# O(N * M) -- space

# No need to have full grid


def rec_graph_dynamic(n, m):
    n, m = max(n, m), min(n, m)
    curr = [1] * m
    prev = [1] * m

    for i in range(1, n):
        curr = [1] * m
        for j in range(1, m):
            curr[j] = curr[j - 1] + prev[j]
        prev = curr

    return curr[-1]


# O(N * M) -- time
# O(min(N, M)) -- space

# Looks like should be formula for that.


def rec_graph(n, m):
    def f(d):
        r = 1
        for i in range(2, d):
            r *= i
        return r

    return f(n + m - 1) // f(n) // f(m)

# O(N + M) -- time
# O(1) -- space
