# Write a function that takes an array of integers
# and returns sorted version of the array using Merge Sort algorithm.
#
# Example
# Input: [15, -2, 4, 1, 0, 9]
# Output: [-2, 0, 1, 4, 9, 15]


def merge_sort(arr):
    b = [el for el in arr]

    def rec(i, j):
        if i + 1 >= j:
            return
        mid = (i + j) // 2
        rec(i, mid)
        rec(mid, j)
        n, m = i, mid
        k = i
        while n < mid and m < j:
            if b[n] < b[m]:
                arr[k] = b[n]
                n += 1
            else:
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

    rec(0, len(arr))
    return arr

# O(NlogN) -- time
# O(N) -- space
