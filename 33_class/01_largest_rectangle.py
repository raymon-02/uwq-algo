# Write a function that takes an array of positive integers
# representing the heights of buildings
# and returns the area of the largest rectangle
# that can be created of adjacent buildings.
#
# Example
# Input: [2, 1, 2, 3, 4]
# Output: 6


def largest_rectangle(buildings):
    result = 0
    stack = []

    for i, el in enumerate(buildings):
        while stack and buildings[stack[-1]] > el:
            h = buildings[stack.pop()]
            dist = i - stack[-1] - 1 if stack else i
            result = max(result, h * dist)
        stack.append(i)

    if not stack:
        return result
    i = stack[-1]
    while stack:
        h = buildings[stack.pop()]
        dist = i - stack[-1] if stack else i + 1
        result = max(result, h * dist)

    return result

# O(N) -- time
# O(N) -- space
