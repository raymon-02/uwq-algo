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

    def rec(i, j):
        result = 0

        if i + 1 >= j:
            return result
        mid = (i + j) // 2
        result += rec(i, mid)
        result += rec(mid, j)
        n, m = i, mid
        k = i
        while n < mid and m < j:
            if b[n] <= b[m]:
                arr[k] = b[n]
                n += 1
            else:
                result += mid - n
                arr[k] = b[m]
                m += 1
            k += 1
        while n < mid:
            arr[k] = b[n]
            n += 1
            k += 1
        while m < j:
            arr[k] = b[m]
            m += 1
            k += 1

        for z in range(i, j):
            b[z] = arr[z]

        return result

    return rec(0, len(arr))

# O(NlogN) -- time
# O(N) -- space
