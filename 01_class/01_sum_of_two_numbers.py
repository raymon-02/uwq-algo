# There are a non-empty array with integers and an integer representing target sum.
# Write a function that check if there are two numbers in the array sum up to the target sum.
# If there are then return these two numbers.
# If there aren't then return None.

from collections import defaultdict


def two_num_sum(arr, target_sum):
    cache = defaultdict(int)
    for el in arr:
        cache[el] += 1
    for el in arr:
        cache[el] -= 1
        if cache.get(target_sum - el, 0) > 0:
            return el, target_sum - el
        cache[el] += 1

    return None

# O(N) -- time
# O(N) -- space
