# There is an array `denoms` of positive integers
# representing coin denominations.
#
# Write a function that takes the array and positive integer
# representing a target amount
# and returns the minimum number of coins needed
# to make change for the target amount
# using the given coin denominations from the array.
# Each coin denomination can be used unlimited amount of time.
#
# Example
# Input: 7, [1, 5, 10]
# Output: 3
# 2 times * 1 + 1 time * 5 = 7
# 2 + 1 = 3


def min_coins_rec(n, denoms):
    def rec(rest, i):
        if rest < 0 or i == len(denoms):
            return float("inf")
        if rest == 0:
            return 0
        take = rec(rest - denoms[i], i) + 1
        leave = rec(rest, i + 1)
        return min(take, leave)

    return rec(n, 0)


# O((N + D)! / N! / D!) -- time
# O(N + D) -- space

# Factorial time without cache.


def min_coins_rec_cache(n, denoms):
    cache = {}

    def rec(rest, i):
        if (rest, i) in cache:
            return cache[(rest, i)]
        if rest < 0 or i == len(denoms):
            return float("inf")
        if rest == 0:
            return 0
        take = rec(rest - denoms[i], i) + 1
        leave = rec(rest, i + 1)
        res = min(take, leave)
        cache[(rest, i)] = res
        return res

    return rec(n, 0)


# O(N * D) -- time
# O(N * D) -- space

# Still recursive. Stack problem.


def min_coins_grid(n, denoms):
    grid = [[float("inf")] * len(denoms) for _ in range(n + 1)]
    grid[0] = [0] * len(denoms)
    for i in range(1, n + 1):
        for j in range(len(denoms)):
            take = grid[i - denoms[j]][j] + 1 if i >= denoms[j] else float("inf")
            leave = grid[i][j - 1] if j > 0 else float("inf")
            grid[i][j] = min(take, leave)

    return grid[-1][-1]


# O(N * D) -- time
# O(N * D) -- space

# No need to have full grid.


def min_coins(n, denoms):
    grid = [float("inf")] * (n + 1)
    grid[0] = 0
    for j in range(len(denoms)):
        for i in range(1, n + 1):
            if i >= denoms[j]:
                grid[i] = min(grid[i], grid[i - denoms[j]] + 1)

    return grid[-1]

# O(N * D) -- time
# O(N) -- space
