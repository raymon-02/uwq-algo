# You have an array of positive integers representing the values of coins.
# Write a function that returns the minimum amount of change (the minimum sum of money)
# that you cannot create.


def non_constructible_number(arr):
    if not arr:
        return 1
    arr.sort()
    curr = 0
    for el in arr:
        if el > curr + 1:
            return curr + 1
        curr += el

    return curr + 1

# O(NlogN) -- time
# O(1) -- space
