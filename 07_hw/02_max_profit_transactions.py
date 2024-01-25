# There is an array `prices` of positive integers
# representing the prices of single stock for n days.
#
# Write a functions that takes an array `prices` and positive k
# and returns maximum profit that is possible to make
# using k transactions and holding one share of the stock at a time.
# One transaction means buy stock on one day and sell it on another.
#
# Example
# Input: [5, 11, 3, 50, 60, 90], 2
# Output: 93
# Buy 5, sell 11 => profit is 6
# Buy 3, sell 90 => profit is 87
# Total profit is 6 + 87 = 93


def max_profit_grid(prices, k):
    if not prices:
        return 0

    grid = [[0] * len(prices) for _ in range(k + 1)]

    for i in range(1, k + 1):
        m = float("-inf")
        for j in range(1, len(prices)):
            m = max(m, grid[i - 1][j - 1] - prices[j - 1])
            grid[i][j] = max(grid[i][j - 1], m + prices[j])

    return grid[-1][-1]


# O(N * k) -- time
# O(N * k) -- space

# No need to have full grid.


def max_profit(prices, k):
    if not prices:
        return 0

    curr = [0] * len(prices)
    prev = [0] * len(prices)

    for i in range(1, k + 1):
        m = float("-inf")
        curr = [0] * len(prices)
        for j in range(1, len(prices)):
            m = max(m, prev[j - 1] - prices[j - 1])
            curr[j] = max(curr[j - 1], m + prices[j])
        prev = curr

    return curr[-1]

# O(N * k) -- time
# O(N) -- space
