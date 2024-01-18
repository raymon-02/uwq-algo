# Write a function that takes two strings
# and returns minimum number of edit operations to perform
# on the first string to ger the second string.
# Edit operations are:
# - insert a char at any position
# - delete a cher at any position
# - substitute a char at any position with another char
#
# Example
# Input: "abc", "xabd"
# Output: 2
# The first operation is add 'x' at 0 position
# The second operation is substitute 'c' with 'd'


def levenshtein_distance_grid(str1, str2):
    str1 = "." + str1
    str2 = "." + str2
    n = len(str1)
    m = len(str2)
    grid = [[i + j for j in range(m)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = min(
                grid[i - 1][j] + 1,
                grid[i][j - 1] + 1,
                grid[i - 1][j - 1] + (str1[i] != str2[j])
            )

    return grid[n - 1][m - 1]


# O(N * M) -- time
# O(N * M) -- space

# No need to have full grid.


def levenshtein_distance(str1, str2):
    str1 = "." + str1
    str2 = "." + str2
    n = len(str1)
    m = len(str2)
    if n < m:
        str1, str2 = str2, str1
        n, m = m, n
    curr = [0] * m
    prev = [j for j in range(m)]

    for i in range(1, n):
        curr = [i] * m
        for j in range(1, m):
            curr[j] = min(
                curr[j - 1] + 1,
                prev[j] + 1,
                prev[j - 1] + (str1[i] != str2[j])
            )
        prev = curr

    return curr[m - 1]

# O(N * M) -- time
# O(min(N, M)) -- space
