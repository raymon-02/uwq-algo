# There is an array `denoms` of positive integers
# representing coin denominations.
#
# Write a function that takes the array and positive integer
# representing a target amount
# and returns the number of ways
# to make change for the target amount
# using the given coin denominations from the array.
# Each coin denomination can be used unlimited amount of time.
#
# Example
# Input: 6, [1, 5]
# Output: 2
# 1 time * 1 + 1 time * 5 = 6  => 1
# 6 times * 1 = 6              => 1
# Total ways 1 + 1 = 2


def way_coins_rec(n, denoms):
    def rec(rest, i):
        if rest < 0 or i == len(denoms):
            return 0
        if rest == 0:
            return 1
        take = rec(rest - denoms[i], i)
        leave = rec(rest, i + 1)
        return take + leave

    return rec(n, 0)


# O((N + D)! / N! / D!) -- time
# O(max(N, D)) -- space

# Factorial time without cache.


def way_coins_rec_cache(n, denoms):
    cache = {}

    def rec(rest, i):
        if (rest, i) in cache:
            return cache[(rest, i)]
        if rest < 0 or i == len(denoms):
            return 0
        if rest == 0:
            return 1
        take = rec(rest - denoms[i], i)
        leave = rec(rest, i + 1)
        res = take + leave
        cache[(rest, i)] = res
        return res

    return rec(n, 0)


# O(N * D) -- time
# O(N * D) -- space

# Still recursive. Stack problem.


def way_coins_grid(n, denoms):
    grid = [[0] * len(denoms) for _ in range(n + 1)]
    grid[0] = [1] * len(denoms)
    for i in range(1, n + 1):
        for j in range(len(denoms)):
            take = grid[i - denoms[j]][j] if i - denoms[j] >= 0 else 0
            leave = grid[i][j - 1] if j > 0 else 0
            grid[i][j] = take + leave

    return grid[-1][-1]


# O(N * D) -- time
# O(N * D) -- space

# No need to have full grid.


def way_coins(n, denoms):
    grid = [0] * (n + 1)
    grid[0] = 1
    for j in range(len(denoms)):
        for i in range(1, n + 1):
            if i >= denoms[j]:
                grid[i] += grid[i - denoms[j]]

    return grid[-1]

# O(N * D) -- time
# O(N) -- space
