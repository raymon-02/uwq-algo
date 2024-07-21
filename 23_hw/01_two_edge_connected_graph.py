# Write a function that takes graph in adjacency format
# and returns boolean representing if the graph is two edge connected.
#
# A graph is called two edge connected
# if it stays connected after removal any edge from it.
#
# Example
# Input: [
#   [1, 2, 5],
#   [0, 2],
#   [0, 1, 3],
#   [2, 4, 5],
#   [3, 5],
#   [0, 3, 4]
# ]
# Output: True


def two_edge_connected(graph):
    time_in = [-1] * len(graph)

    def dfs(v, prev, time):
        time_in[v] = time
        v_time = time

        for to in graph[v]:
            if to == prev:
                continue
            if time_in[to] != -1:
                v_time = min(v_time, time_in[to])
            else:
                to_time = dfs(to, v, time + 1)
                v_time = min(v_time, to_time)

        if v_time == time and prev != -1:
            return -1

        return v_time

    if dfs(0, -1, 0) == -1:
        return False

    return all(map(lambda el: el >= 0, time_in))

# O(V + E) -- time
# O(V) -- space
