# Write a function that takes binary search tree and integer value k
# and returns the kth largest integer in the tree.
# There are more or equal k elements in the tree.
# Duplicate integer values in the tree should be considered at different values.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example
# Input:
#        5
#     /    \
#    3      8
#   / \    / \
#  1   4  7  14
# k = 3
#
# Output: 7


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def k_largest_value(tree, k):
    result = None
    i = 0

    def rec(node):
        nonlocal result
        nonlocal i
        if result or not node:
            return
        rec(node.right)
        i += 1
        if i == k:
            result = node.value
        rec(node.left)

    rec(tree)

    return result

# O(k) -- time
# O(logN) -- space
