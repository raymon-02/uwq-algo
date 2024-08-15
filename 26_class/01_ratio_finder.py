# There is an array consisting of triples.
# Each triple represents original unit, destination unit
# and multiplier between them.
#
# Write a function that takes the array and two units
# and returns the conversion rate between them.
#
# Example:
# Input: [("foot", "yard", 0.333), ("foot", "inch", 12)], "inch", "yard"
# Output: 0.0277


def ratio_finder_dfs(rates, start, end):
    graph = {}
    for orig, dest, rate in rates:
        if orig not in graph:
            graph[orig] = []
        graph[orig].append((dest, rate))
        if dest not in graph:
            graph[dest] = []
        graph[dest].append((orig, 1.0 / rate))

    visited = set()

    def dfs(node, rate_from_orig):
        if node == end:
            return rate_from_orig

        visited.add(node)

        for dest, rate in graph.get(node, []):
            if dest not in visited:
                result = dfs(dest, rate_from_orig * rate)
                if result is not None:
                    return result
        return None

    return dfs(start, 1.0)


# O(V + E) -- time
# O(V + E) -- space

# DFS finds not the shortest path between units.


from collections import deque


def ratio_finder_bfs(rates, start, end):
    graph = {}
    for orig, dest, rate in rates:
        if orig not in graph:
            graph[orig] = []
        graph[orig].append((dest, rate))
        if dest not in graph:
            graph[dest] = []
        graph[dest].append((orig, 1.0 / rate))

    queue = deque()
    visited = set()

    queue.append((start, 1.0))
    visited.add(start)
    while queue:
        node, rate_from_orig = queue.popleft()
        if node == end:
            return rate_from_orig
        for dest, rate in graph.get(node, []):
            if dest not in visited:
                queue.append((dest, rate_from_orig * rate))
                visited.add(node)

    return None


# O(V + E) -- time
# O(V + E) -- space

# No possibility to answer in constant time.


def ratio_finder(rates, start, end):
    graph = {}
    for orig, dest, rate in rates:
        if orig not in graph:
            graph[orig] = []
        graph[orig].append((dest, rate))
        if dest not in graph:
            graph[dest] = []
        graph[dest].append((orig, 1.0 / rate))

    conversions = {}

    def bfs(start_node):
        queue = deque()
        queue.append(start_node)
        conversions[start_node] = (start_node, 1.0)
        while queue:
            node = queue.popleft()
            _, rate_from_orig = conversions[node]
            for dest, rate in graph.get(node, []):
                if dest not in conversions:
                    queue.append(dest)
                    conversions[dest] = (start_node, rate_from_orig * rate)

    for node in graph.keys():
        if node not in conversions:
            bfs(node)

    start_root, start_rate = conversions[start]
    end_root, end_rate = conversions[end]

    if start_root != end_root:
        return None

    return end_rate / start_rate

# O(V + E) -- time
# O(V + E) -- space
