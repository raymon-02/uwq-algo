# You are given a description of a two-lane road.
# l1 and l2 are strings and represent the first and the second lane accordingly.
# Each lane consists of N segments of equal length.
# The k-th segment of the lane can be '.' denotes a smooth segment of a road
# or 'X' denotes a segment containing potholes.
# Cars can drive over segments with potholes, but it is rather uncomfortable.
# Therefore, a project to repair as many potholes as possible was submitted.
# At most one contiguous stretch of each lane may be repaired at a time.
# For the time of reparation those stretches will be closed to traffic.
# How many road segments with potholes can be repaired given that the road must be kept open?
# In other words, stretches of roadworks must not prevent travel from one end of the road to the other.
#
# Example
# Input: "..XX.X.", "X.X.X.."
# Output: 4
# It is possible to repair three potholes in the first lane and the first pothole in the second lane
# without closing the road to traffic.
#
# Example
# Input: ".XXX...X", "..X.XXXX"
# Output: 6
#
# Example
# Input: "XXXXX", ".X..X"
# Output: 5
#
# Example
# Input: "X...X", "..X.."
# Output: 2


def road_path(l1, l2):
    def x_in_str(l):
        return l.count("X")

    def calc(s1, s2):
        res = 0
        x1 = x_in_str(s1)
        x2 = 0
        for i in range(-1, len(s1)):
            i2 = i - 1
            if i2 >= 0 and s2[i2] == "X":
                x2 += 1
            if i >= 0 and s1[i] == "X":
                x1 -= 1
            res = max(res, x1 + x2)
        return res

    return max(calc(l1, l2), calc(l2, l1))

# O(N) -- time
# O(1) -- space
