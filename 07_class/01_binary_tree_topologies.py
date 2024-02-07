# Write a function that takes a positive integer n
# and returns the number of possible binary tree topologies
# that can be created with n nodes.
#
# Example
# Input: 2
# Output: 2
# One node is root.
# When the rest node is a left subtree  => 1
# When the rest node is a right subtree => 1

def binary_tree_topologies_rec(n):
    cache = {}

    def rec(k):
        if k in cache:
            return cache[k]
        if k == 0:
            return 1
        result = 0
        for i in range(k):
            result += rec(i) * rec(k - i - 1)
        cache[k] = result
        return result

    return rec(n)


# O(N^2) -- time
# O(N) -- space


def binary_tree_topologies(n):
    # Catalan number
    # (2n)! / (n! * (n + 1)!)
    up = 1
    for i in range(n + 1, 2 * n + 1):
        up *= i
    down = 1
    for i in range(1, n + 2):
        down *= i

    return up // down

# O(N) -- time
# O(1) -- space
