# Write a function that takes directed graph in adjacency format
# and returns strongly connected components in the graph.
#
# Example
# Input: [
#   [1, 2],
#   [3],
#   [3],
#   [0],
#   [5],
#   []
# ]
# Output: [[0, 1, 2, 3], [4], [5]]


def strongly_connected_components(graph):
    graph_tr = [[] for _ in graph]
    for v, edges in enumerate(graph):
        for to in edges:
            graph_tr[to].append(v)

    result = []
    order = []
    visited = set()

    def dfs(v):
        visited.add(v)
        for to in graph[v]:
            if to not in visited:
                dfs(to)
        order.append(v)

    def dfs_tr(v):
        visited.add(v)
        comp.append(v)
        for to in graph_tr[v]:
            if to not in visited:
                dfs_tr(to)

    for v in range(len(graph)):
        if v not in visited:
            dfs(v)

    visited.clear()

    for i in range(len(graph)):
        v = order[-i - 1]
        if v not in visited:
            comp = []
            dfs_tr(v)
            result.append(comp)

    return result

# O(V + E) -- time
# O(V) -- space
