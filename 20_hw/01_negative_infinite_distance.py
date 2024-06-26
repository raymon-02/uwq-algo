# Write a function that takes connected weighted directed graph in adjacency format
# and returns all pairs of vertices between each there is no minimal path.
# No minimal paths between two vertices means
# that distance between these two vertices can be negative infinitely.
#
# Example
# Input: [
#   [(1, -2), (2, 1)],
#   [(3, 1)],
#   [(1, 2)],
#   [(2, -4)]
# ]
# Output: [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# Floyd-Warshall algo
def negative_infinite_distance(graph):
    n = len(graph)
    d = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for v, edges in enumerate(graph):
        for to, dist in edges:
            d[v][to] = dist

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    result = set()
    for i in range(n):
        for j in range(n):
            for t in range(n):
                if d[i][t] < float("inf") and d[t][t] < 0 and d[t][j] < float("inf"):
                    result.add((i, j))

    return list(result)

# O(V^3) -- time
# O(V^2) -- space
