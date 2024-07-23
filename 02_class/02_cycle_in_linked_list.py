# You have a linked list starting cycling at some node.
#
# Example:
#  1 - 2 - 3 - 4 - 5
#          |       |
#          8 - 7 - 6
#
# The linked list is 1->2->3->4->5->6->7->8->3->4->...goes to cycle.
#
# Write a function that takes such linked list and returns the first node in a cycle.
# In the example above it would be node 3.
#
# Each node in a linked list has type Node containing reference to the next node.
# As an input you have a reference to the first node in a linked list.


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def first_cycle_node(head):
    curr1 = head
    curr2 = head.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next.next

    head1 = head
    head2 = curr1
    end = curr1

    l1 = 0
    curr = head1
    while curr != end:
        curr = curr.next
        l1 += 1

    l2 = 1
    curr = head2.next
    while curr != end:
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

# O(N) -- time
# O(1) -- space
