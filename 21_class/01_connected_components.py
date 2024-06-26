# Write a function that takes graph in adjacency format
# and returns connected components in the graph.
#
# Example
# Input: [
#   [1, 2],
#   [0, 2],
#   [0, 1],
#   [4],
#   [3]
# ]
# Output: [[0, 1, 2], [3, 4]]


def connected_components(graph):
    result = []
    visited = set()

    def dfs(v):
        visited.add(v)
        comp.append(v)
        for to in graph[v]:
            if to not in visited:
                dfs(to)

    for v in range(len(graph)):
        if v not in visited:
            comp = []
            dfs(v)
            result.append(comp)

    return result

# O(V + E) -- time
# O(V) -- space
