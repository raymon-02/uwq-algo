# Write a function that takes an array of integers
# and an array of requests where each request is a pair (l, r)
# and returns an array where each element is
# a sum of values in the array between indices l and r inclusive
# for each request.
#
# Example
# Input: [5, 0, -3, 12, 3, 1], [(0, 3), (5, 5), (2, 4)]
# Example: [14, 1, 12]


def array_sum(arr, requests):
    tree = []
    current = 0
    for el in arr:
        current += el
        tree.append(current)

    result = []
    for l, r in requests:
        res = tree[r]
        res -= tree[l - 1] if l > 0 else 0
        result.append(res)

    return result


# O(N + R) -- time
# O(N + R) -- space


# Write a function that takes array of integers
# and array of requests where each request
# is a string representing type of the request and a pair of two integers.
#
# If type of the request is "search" with pair (l, r) then
# a sum of values in the array between indices l and r inclusive
# should be added into result array.
#
# If type of the request is "update" with pair (i, val) then
# element at index i in the array should be updated with value val.
#
# Example
# Input:
#   [5, 0, -3, 12, 3, 1],
#   [
#     ("search", (1, 4)),
#     ("update", (1, -4)),
#     ("update", (2, 2)),
#     ("search", (1, 4))
#   ]
# Example: [12, 13]


def segment_tree_sum(arr, requests):
    tree = [None] * 4 * len(arr)

    def build(v, tl, tr):
        if tl == tr:
            tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            build(v * 2 + 1, tl, tm)
            build(v * 2 + 2, tm + 1, tr)
            tree[v] = tree[v * 2 + 1] + tree[v * 2 + 2]

    def search(v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return tree[v]
        tm = (tl + tr) // 2
        rl = search(v * 2 + 1, tl, tm, l, min(r, tm))
        rr = search(v * 2 + 2, tm + 1, tr, max(l, tm + 1), r)
        return rl + rr

    def update(v, tl, tr, i, val):
        if tl == tr:
            tree[v] = val
        else:
            tm = (tl + tr) // 2
            if i <= tm:
                update(v * 2 + 1, tl, tm, i, val)
            else:
                update(v * 2 + 2, tm + 1, tr, i, val)
            tree[v] = tree[v * 2 + 1] + tree[v * 2 + 2]

    tree_l, tree_r = 0, len(arr) - 1
    build(0, tree_l, tree_r)
    result = []
    for type, (p1, p2) in requests:
        if type == "search":
            res = search(0, tree_l, tree_r, p1, p2)
            result.append(res)
        else:
            update(0, tree_l, tree_r, p1, p2)

    return result

# O(N + R * logN) -- time
# O(N + logN + R) -- space
