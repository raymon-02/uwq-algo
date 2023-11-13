# Write a function that takes a head of a linked list and an integer k,
# rearranges the list in place around nodes with value k and returns its new head.
# Rearranging means moving all nodes with a value smaller than k
# before all nodes with value k and moving all nodes with a value greater than k
# after all nodes with value k.
# All moved nodes should maintain their original relative ordering.
#
# Each node in the linked list has type Node containing integer value
# and a reference to the next node.
#
# Example
# Input: 3 -> 0 -> 5 -> 2 -> 1 -> 4, 3
# Output: 0 -> 2 -> 1 -> 3 -> 5 -> 4


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def rearrange(head, k):
    pass
