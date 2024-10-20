# Write a function that takes a matrix of booleans
# where each boolean represents piece of land used or not used
# and returns the area of largest rectangle of not used land.
#
# Example
# Input: [
#   [False, True,  True,  True,  False ],
#   [False, False, False, True,  False ],
#   [False, False, False, False, False ],
#   [False, True,  True,  True,  True  ],
# ]
# Output: 6


def largest_park(land):
    heights = [0] * len(land[0])
    result = 0

    def calc():
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                res = max(res, h * w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1 if stack else len(heights)
            res = max(res, h * w)

        return res

    for row in land:
        for i, used in enumerate(row):
            heights[i] = heights[i] + 1 if not used else 0
        result = max(result, calc())

    return result

# O(N * M) -- time
# O(M) -- space
