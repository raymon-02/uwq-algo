# There are n pillars with different heights and width of 1.
# Water pours over all the pillars.
#
# Write a function that takes an array of non-negative integers
# representing the heights of the pillars
# and returns an amount of water trapped between pillars.
#
# Example
# Input: [0, 3, 2, 1, 4, 1, 2]
# Output: 4
# Image with pillars where | is part of a pillar and X means water.
# There are 4 X.
#
#     |
#  |XX|
#  ||X|X|
# _||||||


def water_area(heights):
    def get_max(arr):
        res = []
        m = -1
        for el in arr:
            m = max(m, el)
            res.append(m)
        return res

    ml = get_max(heights)
    mr = get_max(reversed(heights))

    result = 0
    for el, l, r in zip(heights, ml, reversed(mr)):
        result += min(l, r) - el

    return result


# O(N) -- time
# O(N) -- space


def water_area_idx(heights):
    if not heights:
        return 0

    i = 0
    j = len(heights) - 1
    el = heights[i]
    er = heights[j]
    result = 0

    while i < j:
        if el < er:
            i += 1
            el = max(el, heights[i])
            result += el - heights[i]
        else:
            j -= 1
            er = max(er, heights[j])
            result += er - heights[j]

    return result

# O(N) -- time
# O(1) -- space
