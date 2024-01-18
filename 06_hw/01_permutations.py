# Write a function that takes an array of unique integers
# and returns all possible permutations of the array.
#
# Example
# Input: [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def permutations(arr):
    result = []
    n = len(arr)
    if not n:
        return result

    def rec(curr, path):
        if len(path) == n:
            result.append(path)
            return
        for el in [*curr]:
            curr.remove(el)
            p = [e for e in path]
            p.append(el)
            rec(curr, p)
            curr.add(el)

    rec(set(arr), [])

    return result

# O(N^2 * N!) -- time
# O(N * N!) -- space
