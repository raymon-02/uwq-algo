# You have two non-empty linked lists merged together at some node
# meaning that these two lists have common ending.
#
# Example:
#  1 - 2 - 3 - 4 - 5
#          |
#  6 - 7 - 8
#
# The first linked list is 1->2->3->4->5
# The second linked list is 6->7->8->3->4->5
# The common ending is 3->4->5
#
# Write a funtion that takes such two linked lists and returns the first common node.
# In the example above it would be node 3.
#
# Each node in linked lists has type Node containing reference to the next node
# or None value if it is the last node in the list.
# As an input you have two references to the first nodes in each linked list.


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def first_common_node(head1, head2):
    l1 = 0
    curr = head1
    while curr:
        curr = curr.next
        l1 += 1

    l2 = 0
    curr = head2
    while curr:
        curr = curr.next
        l2 += 1

    if l1 < l2:
        head1, head2 = head2, head1
        l1, l2 = l2, l1

    curr1 = head1
    for _ in range(l1 - l2):
        curr1 = curr1.next
    curr2 = head2
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next

    return curr1

# O(N + M) -- time
# O(1) -- space
