# Write a function that takes a binary tree and returns its max path sum.
# A path is collection of connected nodes in a tree.
# A path sum is a sum of the values of the nodes in a particular path.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example:
#        5
#     /    \
#   -10     3
#   / \    / \
#  4   7  12  2
#
# The max path sum is 20. The path is 5-3-12
#
# Example:
#        5
#     /    \
#   -10     3
#   / \    / \
#  4   7  12  9
#
# The max path sum is 24. The path is 12-3-9
#
# In both examples input is a link to the root Node with value 5


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(tree):
    result = float("-inf")

    def rec(node):
        nonlocal result
        lr = rec(node.left) if node.left else float("-inf")
        rr = rec(node.right) if node.right else float("-inf")

        res = max(lr + node.value, rr + node.value, node.value)
        result = max(result, res, lr + node.value + rr)

        return res

    rec(tree)

    return result

# O(N) -- time
# O(logN) -- space
