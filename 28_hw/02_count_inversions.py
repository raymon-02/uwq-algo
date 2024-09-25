# Write a function that takes an array of integers
# and returns the number of inversions in the array.
#
# The inversion occurs when for index i and j
# i < j and arr[i] > arr[j].
#
# Example
# Input: [3, 4, 1, 2]
# Output: 4
# There are 4 inversions. Indices are (0, 2), (0, 3), (1, 2), (1, 3)


def count_inversions(arr):
    b = [el for el in arr]

    def rec(l, r):
        result = 0

        if l + 1 >= r:
            return result
        m = (l + r) // 2
        result += rec(l, m)
        result += rec(m, r)
        i, j, k = l, m, l
        while i < m and j < r:
            if b[i] <= b[j]:
                arr[k] = b[i]
                i += 1
            else:
                result += m - i
                arr[k] = b[j]
                j += 1
            k += 1
        while i < m:
            arr[k] = b[i]
            i += 1
            k += 1
        while j < r:
            arr[k] = b[j]
            j += 1
            k += 1

        for k in range(l, r):
            b[k] = arr[k]

        return result

    return rec(0, len(arr))

# O(NlogN) -- time
# O(N) -- space
