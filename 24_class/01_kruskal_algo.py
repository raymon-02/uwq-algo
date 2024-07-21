# Write a function that takes weighted graph in adjacency format
# and returns a graph in adjacency format representing minimum spanning tree of the initial graph.
#
# A minimum spanning tree of the graph is a tree containing all vertices and subset of edges.
# These edges should connect all vertices with minimum total edge weight and without cycles.
#
# The function should implement Kruskal algorithm.
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


def kruskal_algo(graph):
    edges = []
    for v, tos in enumerate(graph):
        for to, w in tos:
            if v < to:
                edges.append((w, (v, to)))
    edges.sort()

    tree = [i for i in range(len(graph))]
    result = [[] for _ in graph]
    for w, (v, to) in edges:
        if tree[v] != tree[to]:
            result[v].append((to, w))
            result[to].append((v, w))
            old_group = tree[v]
            new_group = tree[to]
            for j in range(len(graph)):
                if tree[j] == old_group:
                    tree[j] = new_group

    return result


# O(ElogE + V^2) -- time
# O(V + E) -- space

# Tree union can be improved using disjoint-set.


def kruskal_algo_dsu(graph):
    dsu = {}

    def create(x):
        dsu[x] = x

    def find(x):
        if x not in dsu:
            create(x)
        if dsu[x] == x:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        dsu[ry] = rx

    edges = []
    for v, tos in enumerate(graph):
        for to, w in tos:
            if v < to:
                edges.append((w, (v, to)))
    edges.sort()

    result = [[] for _ in graph]
    for w, (v, to) in edges:
        root_v = find(v)
        root_to = find(to)
        if root_v != root_to:
            result[v].append((to, w))
            result[to].append((v, w))
            union(v, to)

    return result

# O(ElogE) -- time
# O(V + E) -- space
