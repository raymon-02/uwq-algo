# Write a function that takes an array of unique integers
# and returns its powerset.
# Powerset means set of all possible subsets.
#
# Example
# Input: [1, 2, 3]
# Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


def powerset(arr):
    result = [[]]

    n = len(arr)
    i = 1
    curr = "0" * n
    end = "1" * n

    while curr != end:
        add = []
        curr = "{0:b}".format(i).zfill(n)
        for b, el in zip(curr, arr):
            if int(b) == 1:
                add.append(el)
        result.append(add)
        i += 1

    return result

# O(N * 2^N) -- time
# O(N * 2^N) -- space
