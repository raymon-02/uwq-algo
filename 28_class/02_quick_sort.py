# Write a function that takes an array of integers
# and returns sorted version of the array using Quick Sort algorithm.
#
# Example
# Input: [15, -2, 4, 1, 0, 9]
# Output: [-2, 0, 1, 4, 9, 15]


def quick_sort(arr):
    def rec(l, r):
        if l + 1 >= r:
            return

        m = 0
        for i in range(l + 1, r):
            if arr[i] < arr[l]:
                m += 1
        m += l
        arr[l], arr[m] = arr[m], arr[l]
        i, j = l, r - 1
        while i != m and j != m:
            while i != m and arr[i] < arr[m]:
                i += 1
            while j != m and arr[j] >= arr[m]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        rec(l, m)
        rec(m + 1, r)

    rec(0, len(arr))

    return arr

# O(NlogN) -- time
# O(logN) -- space
