# There is a matrix where each element at position (i, j)
# represents exchange rate between currency i and currency j.
# Exchange rate between currency i and i always equals to 1.
# Write a function that takes the matrix and returns
# if arbitrage trading is possible using exchange rates from the matrix.
# Arbitrage trading means you can start with X units of one currency
# and get more than X units of the same currency performing a series of exchanges.
#
# Example
# Input: [
#   [1.0000, 0.8631, 0.5903],
#   [1.1586, 1.0000, 0.6849],
#   [1.6939, 1.4600, 1.0000]
# ]
# Output: True


from math import log


def arbitrage_trading(rates):
    n = len(rates)
    grid = [[-log(el) for el in row] for row in rates]
    d = [0] * n

    result = False
    for _ in range(n):
        result = False
        for i in range(n):
            for j in range(n):
                if d[j] > d[i] + grid[i][j]:
                    d[j] = d[i] + grid[i][j]
                    result = True

    return result

# O(N^3) -- time
# O(N^2) -- space
