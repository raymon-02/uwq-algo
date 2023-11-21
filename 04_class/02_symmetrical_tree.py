# Write a function that takes a binary tree and checks
# if this binary tree is symmetrical.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example
# Input:
#        5
#     /    \
#    3      3
#   / \    / \
#  4   7  7   4
#
# Output: True


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def symmetrical_tree(tree):
    def rec(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return rec(node1.left, node2.right) and rec(node1.right, node2.left)

    return rec(tree.left, tree.right)

# O(N) -- time
# O(logN) -- space
