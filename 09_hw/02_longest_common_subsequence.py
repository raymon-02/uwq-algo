# Write a function that takes two strings
# and returns their longest common subsequence.
#
# Example
# Input: "YXYZZYXV", "XXZYXXYV"
# Output: "XZYXV"


def longest_common_subsequence(str1, str2):
    str1 = "." + str1
    str2 = "." + str2
    grid = [[0] * len(str2) for _ in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

    result = []
    i = len(str1) - 1
    j = len(str2) - 1
    while i != 0 and j != 0:
        if grid[i][j] == grid[i - 1][j]:
            i -= 1
        elif grid[i][j] == grid[i][j - 1]:
            j -= 1
        else:
            result.append(str1[i])
            i -= 1
            j -= 1

    return list(reversed(result))

# O(N * M) -- time
# O(N * M) -- space
