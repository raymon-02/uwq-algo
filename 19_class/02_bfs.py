# Write a function that takes connected graph in adjacency format
# and returns graph vertices in breadth-first-search traversing order.
#
# Example
# Input: [[1, 2], [2], []]
# Output: [0, 1, 2]


from collections import deque


def bfs(graph):
    queue = deque()
    visited = set()
    result = []

    queue.append(0)
    visited.add(0)
    result.append(0)
    while queue:
        v = queue.popleft()
        for to in graph[v]:
            if to not in visited:
                queue.append(to)
                visited.add(to)
                result.append(to)

    return result

# O(V + E) -- time
# O(V) -- space
