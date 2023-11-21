# Write a function that takes a binary tree and inverts.
# In other words children for each node should be swapped.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example
# Input:
#        5
#     /    \
#   -10     3
#   / \    / \
#  4   7  12  2
#
# Output:
#        5
#     /    \
#    3     -10
#   / \    / \
#  2  12  7   4


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(tree):
    def rec(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        rec(node.left)
        rec(node.right)

    rec(tree)

# O(N) -- time
# O(logN) -- space
