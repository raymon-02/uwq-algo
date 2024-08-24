# Write a function that takes an array of distinct integers and positive integer k
# and returns the kth smallest integer in the array.
#
# Example
# Input: [15, -2, 4, 1, 0, 9], 3
# Output: 1


def quickselect(arr, k):
    k -= 1

    def rec(l, r):
        m = 0
        for i in range(l + 1, r):
            if arr[i] < arr[l]:
                m += 1
        m += l
        arr[l], arr[m] = arr[m], arr[l]

        if m == k:
            return arr[m]

        i, j = l, r - 1
        while i != m and j != m:
            while arr[i] < arr[m]:
                i += 1
            while arr[j] > arr[m]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        if k < m:
            return rec(l, m)
        else:
            return rec(m + 1, r)

    return rec(0, len(arr))

# O(N) -- time
# O(logN) -- space
