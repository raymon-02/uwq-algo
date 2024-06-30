# There are a list of string representing name of airports,
# list of pairs of strings representing routes between two airports
# and string representing starting airport.
# Write a function that takes these two lists and string
# and returns the minimum number of routes that needs to be added
# to be able to reach any airport in the list starting from the starting airport.
#
# Example
# Input:
# ["LED", "PEE", "FCO, ""BER", "SFO"]
# [
#   ["PEE", "LED"],
#   ["LED", "PEE"],
#   ["BER", "SFO"],
#   ["SFO", "FCO"]
# ],
# "PEE"
# Output: 1
# Needs to add route ["PEE", "BER"] or ["PEE", "LED"]
# to be able to reach any airport from the list.


from collections import defaultdict, Counter


def airport_connections(airports, routes, start):
    graph = defaultdict(set)
    for v, to in routes:
        graph[v].add(to)

    def dfs(v, visited):
        if v in visited:
            return
        visited.add(v)
        for to in graph[v]:
            dfs(to, visited)
        return visited

    reachable = set()
    dfs(start, reachable)
    rest = set(airports) - reachable

    result = 0
    c = Counter()
    for v in rest:
        c[v] = len(dfs(v, set()))
    visited = set()
    for v, _ in sorted(c.items(), key=lambda x: x[1], reverse=True):
        if v not in visited:
            result += 1
            dfs(v, visited)

    return result

# O(V^2 + V * E + VlogV) -- time
# O(V + E) -- space
