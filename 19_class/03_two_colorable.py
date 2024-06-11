# Write a function that takes connected graph in adjacency format
# and returns boolean representing if graph is two-colorable.
# Graph is two-colorable if all nodes can be assigned one of two colors
# such that no nodes of the same color are connected.
#
# Example
# Input: [[1, 2], [0, 2], [0, 1]]
# Output: False


def two_colorable(graph):
    colors = {0: 0}

    def rec(v):
        for to in graph[v]:
            if to in colors:
                if colors[v] == colors[to]:
                    return False
            else:
                colors[to] = (colors[v] + 1) % 2
                if not rec(to):
                    return False
        return True

    return rec(0)

# O(V + E) -- time
# O(V) -- space
