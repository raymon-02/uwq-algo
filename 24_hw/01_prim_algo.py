# Write a function that takes weighted graph in adjacency format
# and returns a graph in adjacency format representing minimum spanning tree of the initial graph.
#
# A minimum spanning tree of the graph is a tree containing all vertices and subset of edges.
# These edges should connect all vertices with minimum total edge weight and without cycles.
#
# The function should implement Prim algorithm.
#
# Example
# Input: [
#   [(1, 3), (2, 5)],
#   [(0, 3), (2, 10), (3, 12)],
#   [(0, 5), (1, 10)],
#   [(1, 12)]
# ]
# Output: [
#   [(1, 3), (2, 5)],
#   [(0, 3), (3, 12)],
#   [(0, 5)],
#   [(1, 12)]
# ]


def prim_algo(graph):
    used = set()
    min_w_edges = [float("inf")] * len(graph)
    min_w_edges[0] = 0
    to_edges = [-1] * len(graph)
    result = [[] for _ in graph]

    for _ in graph:
        v = -1
        for j in range(len(graph)):
            if j not in used and (v == -1 or min_w_edges[j] < min_w_edges[v]):
                v = j

        used.add(v)

        if to_edges[v] != -1:
            to = to_edges[v]
            result[v].append((to, min_w_edges[v]))
            result[to].append((v, min_w_edges[v]))

        for to, w in graph[v]:
            if to not in used and w < min_w_edges[to]:
                min_w_edges[to] = w
                to_edges[to] = v

    return result


# O(V^2) -- time
# O(V) -- space

# Search next vertex can be improved using heap.


import heapq


def prim_algo_heap(graph):
    used = set()
    heap = []
    heapq.heappush(heap, (0, 0))
    min_w_edges = [float("inf")] * len(graph)
    min_w_edges[0] = 0
    to_edges = [-1] * len(graph)
    result = [[] for _ in graph]

    while heap:
        _, v = heapq.heappop(heap)

        if v not in used:
            used.add(v)

            if to_edges[v] != -1:
                to = to_edges[v]
                result[v].append((to, min_w_edges[v]))
                result[to].append((v, min_w_edges[v]))

            for to, w in graph[v]:
                if to not in used and w < min_w_edges[to]:
                    min_w_edges[to] = w
                    to_edges[to] = v
                    heapq.heappush(heap, (min_w_edges[to], to))

    return result

# O(ElogE + VlogE) -- time
# O(V + E) -- space
#
# Time for the worst case when E=V^2:
# O(ElogE + VlogE) = O(ElogV + VlogV) = O(ElogV) or O(V^2 * logV)
