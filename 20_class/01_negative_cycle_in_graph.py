# Write a function that takes weighted directed graph in adjacency format
# and returns path of any negative cycle in the graph.
# If there is no negative cycle in the graph the function should return empty path.
#
# Example
# Input: [
#   [(1, -2), (2, 1)],
#   [(3, 1)],
#   [(1, 2)],
#   [(2, -4)]
# ]
# Output: [1, 3, 2]


# Bellman-Ford algo
def negative_cycle_in_graph(graph):
    d = [0] * len(graph)
    paths = [-1] * len(graph)
    cycle_v = -1

    for _ in graph:
        cycle_v = -1
        for v, edges in enumerate(graph):
            for to, dist in edges:
                if d[to] > d[v] + dist:
                    d[to] = d[v] + dist
                    paths[to] = v
                    cycle_v = to

    if cycle_v == -1:
        return []

    cycle_start = cycle_v
    for _ in graph:
        cycle_start = paths[cycle_start]

    result = [cycle_start]
    curr = paths[cycle_start]
    while curr != cycle_start:
        result.append(curr)
        curr = paths[curr]

    return list(reversed(result))

# O(V * E) -- time
# O(V) -- space
