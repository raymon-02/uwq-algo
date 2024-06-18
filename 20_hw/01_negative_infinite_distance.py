# Write a function that takes connected weighted directed graph in adjacency format
# and returns all pairs of vertices between which there is no minimal path.
# No minimal paths between two vertices means
# that distance between these two vertices can be infinitely negative.
#
# Example
# Input: [
#   [(1, -2), (2, 1)],
#   [(3, 1)],
#   [(1, 2)],
#   [(2, -4)]
# ]
# Output: [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# Floyd-Warshall algo
def negative_infinite_distance(graph):
    pass
