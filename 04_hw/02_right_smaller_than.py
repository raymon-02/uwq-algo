# Write a function that takes an array `arr` of integers and returns
# an array `output` where each element with index i represents
# the number of elements with index j where j > i and arr[j] < arr[i].
# In other words output[i] represents the number of elements from arr
# which are to the right of i and smaller than arr[i].
#
# Example
# Input: [8, 5, 11, -1, 3, 4, 2]
# Output: [5, 4, 4, 0, 1, 1, 0]
# For index 0. There are 5 elements smaller than 8 to the right. They are: 5, -1, 3, 4, 2 => 5
# For index 1. There are 4 elements smaller than 5 to the right. They are: -1, 3, 4, 2    => 4
# For index 2. There are 4 elements smaller than 11 to the right. They are: -1, 3, 4, 2   => 4
# For index 3. There are 0 elements smaller than -1 to the right.                         => 0
# For index 4. There is 1 element smaller than 3 to the right. It is 2                    => 1
# For index 5. There is 1 element smaller than 4 to the right. It is 2                    => 1
# For index 6. There are 0 elements smaller than 2 to the right.                          => 0
#
# Hint: binary search tree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_smaller_than(arr):
    if not arr:
        return []

    def add(node, val, r):
        if val <= node.val:
            node.count += 1
            if node.left:
                return add(node.left, val, r)
            else:
                node.left = Node(val)
                return r
        else:
            if node.right:
                return add(node.right, val, r + node.count + 1)
            else:
                node.right = Node(val)
                return r + node.count + 1

    result = [0]
    root = Node(arr[-1])
    for el in reversed(arr[:-1]):
        c = add(root, el, 0)
        result.append(c)

    return list(reversed(result))

# O(NlogN) -- time
# O(N) -- space
