# You have two arrays with lengths N and N+M accordingly.
# The first array with length N contains N integers in sorted order.
# The second array with length M+N contains M integers at the first M indexes in sorted order
# and None values at the next N indexes.
# Write a function that takes N, M and such two arrays
# and returns the array of length N+M containing all elements in sorted order from the initial arrays.
# You can modify initial arrays.
#
# Example
# Input: 4, 2, [1, 3, 5, 5], [2, 10, None, None, None, None]
# Output: [1, 2, 3, 5, 5, 10]


def sorted_array(n, m, arr1, arr2):
    i1, i2, ri = n - 1, m - 1, n + m - 1
    while i1 >= 0 and i2 >= 0:
        if arr1[i1] < arr2[i2]:
            arr2[ri] = arr2[i2]
            i2 -= 1
        else:
            arr2[ri] = arr1[i1]
            i1 -= 1
        ri -= 1
    while i1 >= 0:
        arr2[ri] = arr1[i1]
        i1 -= 1
        ri -= 1

    return arr2

# O(N + M) -- time
# O(1) -- space
