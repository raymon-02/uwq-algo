# Write a function that takes an array of unique integers
# and returns all possible permutations of the array.
#
# Example
# Input: [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def permutations(arr):
    result = []
    if not arr:
        return result

    def rec(curr, path):
        if not curr:
            result.append(path.copy())
            return
        for el in [*curr]:
            curr.remove(el)
            path.append(el)
            rec(curr, path)
            path.pop()
            curr.add(el)

    rec(set(arr), [])

    return result

# O(N^2 * N!) -- time
# O(N * N!) -- space
