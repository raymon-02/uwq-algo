# Write a function that takes graph in adjacency format
# and returns graph vertices in depth-first-search traversing order.
#
# Example
# Input: [[1, 2], [2], []]
# Output: [0, 1, 2]


def dfs(graph):
    result = []
    visited = set()

    def rec(v):
        visited.add(v)
        result.append(v)
        for to in graph[v]:
            if to not in visited:
                rec(to)

    for v in range(len(graph)):
        if v not in visited:
            rec(v)

    return result

# O(V + E) -- time
# O(V) -- space
