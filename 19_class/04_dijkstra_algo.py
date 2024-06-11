# Write a function that takes weighted graph with non-negative weights
# in adjacency format and start vertex
# and returns the shortest paths between `start` vertex and all other vertices.
# The function should implement Dijkstra algorithm.
#
# Example
# Input: [[(1, 2), (2, 1)], [(3, 1)], [(3, 1)], []], 0
# Output: [0, 2, 1, 2]


def dijkstra_algo(graph, start):
    d = [float("inf")] * len(graph)
    d[start] = 0
    visited = set()

    for _ in graph:
        v = -1
        for j, _ in enumerate(d):
            if j not in visited and (v == -1 or d[j] < d[v]):
                v = j

        if d[v] == float("inf"):
            return

        visited.add(v)
        for to, dist in graph[v]:
            d[to] = min(d[to], d[v] + dist)

    return d

# O(V^2 + E) -- time
# O(V) -- space
