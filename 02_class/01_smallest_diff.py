# Write a function that takes two non-empty arrays of integers
# and returns the pair of numbers (one from each array)
# whose absolute difference is closest to 0
#
# Example
# Input: [10, 5, -1, 28], [26, 15, 17]
# Output: 28, 26


def smallest_diff(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    i1, i2 = 0, 0
    diff = abs(arr1[0] - arr2[0])
    result = arr1[0], arr2[0]
    while i1 < len(arr1) and i2 < len(arr2):
        nd = abs(arr1[i1] - arr2[i2])
        if nd == 0:
            return arr1[i1], arr2[i2]
        if nd < diff:
            diff = nd
            result = arr1[i1], arr2[i2]
        if arr1[i1] < arr2[i2]:
            i1 += 1
        else:
            i2 += 1

    return result

# O(NlogN + MlogM) -- time
# O(1) -- space
