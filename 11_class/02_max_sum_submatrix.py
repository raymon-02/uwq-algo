# Write a function that takes a matrix (two-dimensional array)
# and positive integer `size`
# and returns the maximum sum that can be generated
# from a sub-matrix with dimensions `size` * `size`.
#
# Example
# Input: [[2, 4], [5, 6], [-3 , 2]], 2
# Output: 17
# Sub-matrox with the maximum sum is [[2, 4], [5, 6]]


def max_sum_submatrix(matrix, size):
    grid = [[0] * len(matrix[0]) for _ in matrix]
    grid[0][0] = matrix[0][0]
    for i in range(1, len(matrix)):
        grid[i][0] = grid[i - 1][0] + matrix[i][0]
    for j in range(1, len(matrix[0])):
        grid[0][j] = grid[0][j - 1] + matrix[0][j]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            grid[i][j] = matrix[i][j] + grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

    result = grid[size - 1][size - 1]
    for i in range(size, len(matrix)):
        result = max(result, grid[i][size - 1] - grid[i - size][size - 1])
    for j in range(size, len(matrix[0])):
        result = max(result, grid[size - 1][j] - grid[size - 1][j - size])
    for i in range(size, len(matrix)):
        for j in range(size, len(matrix[0])):
            result = max(result, grid[i][j] - grid[i - size][j] - grid[i][j - size] + grid[i - size][j - size])

    return result

# O(N * M) -- time
# O(N * M) -- space
