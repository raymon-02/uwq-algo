# You have a reference to not last node in a linked list.
# Write a function that removes this node from the linked list.
# Each node in the linked list has type Node containing integer value
# and a reference to the next node.
# You can modify the value and the next reference of any node.


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def remove_node(node):
    node.val = node.next.val
    node.next = node.next.next

# O(1) -- time
# O(1) -- space
