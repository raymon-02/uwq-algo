# Write a function that takes binary tree and returns
# if the tree is balanced.
# A tree is balanced if for each node in the tree the difference between
# height of the left subtree and the right subtree is 0 or 1.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.

# Example
# Input:
#        5
#     /    \
#    3      2
#   / \
#  4   7
#
# Output: True
#
#
# Example
# Input:
#        5
#     /    \
#    3      2
#   / \
#  4   1
#     / \
#    6   7
#
# Output: False


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree):
    pass
