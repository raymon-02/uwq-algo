# There is a matrix consisting of 0 and 1
# where 0 represents land and 1 represents water.
# An island is any positive number of 0
# that are horizontally or vertically adjacent.
# Write a function that takes the matrix
# and returns the size of the largest possible island
# after changing exactly one 1 to 0.
#
# Example
# Input: [
#   [0, 1, 1],
#   [0, 0, 1],
#   [1, 1, 0]
# ]
# Output: 5
# Changing matrix[1][2] element to 0 creates an island with size 5.


def largest_island(matrix):
    dsu = {}
    size = {}
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def create(x):
        dsu[x] = x
        size[x] = 1

    def find(x):
        if x == dsu[x]:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        dsu[root_y] = root_x
        size[root_x] += size[root_y]

    visited = set()

    def rec(i, j, root):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or (i, j) in visited or matrix[i][j] == 1:
            return
        x = (i, j)
        visited.add(x)
        create(x)
        if not root:
            root = x
        else:
            union(root, x)
        for im, jm in moves:
            rec(i + im, j + jm, root)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rec(i, j, None)

    result = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                res = 1
                roots = set()
                for im, jm in moves:
                    x = (i + im, j + jm)
                    if x in dsu:
                        rx = find(x)
                        if rx not in roots:
                            roots.add(rx)
                            res += size[rx]
                result = max(result, res)

    return result

# O(N * M) -- time
# O(N * M) -- space
