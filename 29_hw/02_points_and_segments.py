# Write a function that takes an array of requests
# where each request is a string representing type of the request
# and a value.
#
# If type of the request is "add" with value x then
# point with coordinate x should be remembered.
#
# If type of the request is "search" with value of pair (l, r) then
# a count of points existing between coordinates l and r inclusive
# should be added into result array.
#
# Point coordinate is an integer x where 0 <= x <= 10^6
#
# Example
# Input:
#   [
#     ("search", (1, 4)),
#     ("add", 1),
#     ("add", 2),
#     ("search", (1, 4))
#     ("search", (2, 100))
#   ]
# Example: [0, 2, 1]


def points_and_segments(requests):
    max_point = 1000000
    tree = [0] * 4 * max_point

    def search(v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return tree[v]
        tm = (tl + tr) // 2
        rl = search(v * 2 + 1, tl, tm, l, min(r, tm))
        rr = search(v * 2 + 2, tm + 1, tr, max(l, tm + 1), r)
        return rl + rr

    def add(v, tl, tr, x):
        if tl == tr:
            tree[v] += 1
        else:
            tm = (tl + tr) // 2
            if x <= tm:
                add(v * 2 + 1, tl, tm, x)
            else:
                add(v * 2 + 2, tm + 1, tr, x)
            tree[v] += 1

    tree_l, tree_r = 0, max_point - 1
    result = []
    for type, r in requests:
        if type == "search":
            l, r = r
            res = search(0, tree_l, tree_r, l, r)
            result.append(res)
        else:
            add(0, tree_l, tree_r, r)

    return result

# O(N + R * logN) -- time
# O(N + logN + R) -- space
# where N is a total number of different coordinates
