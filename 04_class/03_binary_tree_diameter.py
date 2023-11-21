# Write a function that takes a binary tree and returns its diameter.
# The diameter of binary tree is a length of the longest path.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example
# Input:
#          5
#        /   \
#       3     3
#      / \
#     4   7
#    /     \
#   2       1
#  /         \
# 6           8
#
# Output: 7
# The longest path is 6-2-4-3-7-1-8


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def tree_diameter(tree):
    result = 0

    def rec(node):
        nonlocal result
        if not node:
            return 0
        rl = rec(node.left)
        rr = rec(node.right)
        result = max(result, rl + rr)
        return max(rl, rr) + 1

    rec(tree)

    return result

# O(N) -- time
# O(logN) -- space
