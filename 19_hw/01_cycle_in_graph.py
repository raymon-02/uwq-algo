# Write a function that takes graph in adjacency format
# and returns boolean representing if the graph contains a cycle.
#
# Example
# Input: [[1, 2], [2], []]
# Output: False

def cycle_in_graph(graph):
    color = [0] * len(graph)

    def dfs(v):
        if color[v] == 2:
            return False
        if color[v] == 1:
            return True
        color[v] = 1
        for to in graph[v]:
            if dfs(to):
                return True
        color[v] = 2
        return False

    for v in range(len(graph)):
        if dfs(v):
            return True

    return False

# O(V + E) -- time
# O(V) -- space
