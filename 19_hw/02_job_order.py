# There are list of integers representing jobs to complete
# and list of pairs of integers where each pair represents job dependencies.
# The second job in pair depends on the first one.
# Write a function that takes these two arrays
# and returns jobs in valid order to complete.
# If there is no such order the function should return empty array.
#
# Example
# Input: [1, 2, 3, 4], [(1, 2), (1, 3), (3, 2), (4, 2), (4, 3)]
# Output: [4, 1, 3, 2]


from collections import defaultdict


# Topological sort
def job_order(jobs, deps):
    graph = defaultdict(set)
    for v, to in deps:
        graph[to].add(v)

    end = set(jobs)
    for v, _ in deps:
        if v in end:
            end.remove(v)

    visited = set()
    progress = set()
    result = []

    def dfs(v):
        if v in visited:
            return True
        if v in progress:
            return False
        progress.add(v)

        for to in graph[v]:
            if not dfs(to):
                return False
        progress.remove(v)
        visited.add(v)
        result.append(v)

        return True

    for v in end:
        if not dfs(v):
            return []

    return result if len(jobs) == len(visited) else []

# O(V + E) -- time
# O(V + E) -- space
