# Write a function that takes a binary tree and returns a sum
# of all subtree's node's depth.
#
# Each node has type Node which contains integer value
# and links to left Node and right Node.
#
# Example
# Input:
#        5
#     /    \
#    3      2
#   / \
#  4   7
#
# Output: 8
# Sum for Node 4 is 0: this node is leaf => 0
# Sum for Node 7 is 0: this node is leaf => 0
# Sum for Node 3 is 2: to Node 4 and Node 7 depth 1 => 1+1=2
# Sum for Node 5 is 4: to Node 2 and Node 3 depth is 1, to Node 4 and Node 7 depth is 2 => 1+1+2+2=6
# All sums: 0+0+2+6=8


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def all_node_depth(tree):
    pass
