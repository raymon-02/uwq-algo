# Write a function that takes array of integers and returns the second minimum.
# The array can contain duplicate integers.
# The second minimum should be different from the first minimum.
# If there is no second minimum function should return None.
#
# Example
# Input: [10, 4, 2, -9, 15]
# Output: 2
# The first minimum is -9, the second minimum is 2.
#
# Example
# Input: [10, 4, 2, -9, 15, -9, 2, 2, -9]
# Output: 2
# The first minimum is -9, the second minimum is 2.
#
# Example
# Input: [1, 1, 1]
# Output: None
# The first minimum is 1 and there are no more other numbers.


def second_min(arr):
    if not arr:
        return None
    fm = arr[0]
    sm = None
    for el in arr[1:]:
        if el < fm:
            fm, sm = el, fm
        elif el != fm and (sm is None or el < sm):
            sm = el

    return sm


# O(N) -- time
# O(1) -- space


# The same condition as above but function should return kth minimum.
# If there is no kth minimum function should return None.
#
# Example
# Input: [10, 4, 2, -9, 15], 4
# Output: 10
# k equals to 4, then function should return the forth minimum.
# The first minimum is -9, the second minimum is 2, the third minimum is 4, the fourth minimum is 10
#
# Example
# Input: [10, 4, 2, -9, 15, -9, 2, 2, -9], 4
# Output: 10
# k equals to 4, then function should return the forth minimum
# The first minimum is -9, the second minimum is 2, the third minimum is 4, the fourth minimum is 10
#
# Example
# Input: [1, 1, 2, 3, 1], 4
# Output: None
# k equals to 4, then function should return the forth minimum
# The first minimum is 1, the second minimum is 2, the third minimum is 3 and there are no more other numbers.


def kth_min(arr, k):
    if not arr:
        return None
    arr = sorted(arr)
    i = 0
    for _ in range(k - 1):
        if i >= len(arr):
            return None
        curr = arr[i]
        while i < len(arr) and arr[i] == curr:
            i += 1
    if i >= len(arr):
        return None

    return arr[i]

# O(NlogN) -- time
# O(1) -- space
