# Imagine you place a knight chess piece on a phone dial pad.
# This chess piece moves in an uppercase “L” shape.
# Suppose you dial keys on the keypad using only hops a knight can make.
# Every time the knight lands on a key, we dial that key and make another hop.
# The starting position counts as being dialed.
# How many distinct numbers can you dial in N hops from a particular starting position?
#
# Write a function that takes start position and integer N
# and returns count of such possible distinct numbers.


neighbors = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: (),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}


def ns(num):
    return neighbors[num]


def knights_dialer_gen_rec(start, n):
    result = []

    def rec(curr, rest, path):
        if rest == 0:
            result.append(path)
            return
        for ne in ns(curr):
            rec(ne, rest - 1, path + [ne])

    rec(start, n, [])

    return len(result)


# O(N * 3^N) -- time
# O(N * 3^N) -- space

# No need to generate numbers.
# T(P, N) = sum T(p, N - 1) for p in ns(P)


def knights_dialer_rec(start, n):
    def rec(curr, rest):
        if rest == 0:
            return 1
        res = 0
        for ne in ns(curr):
            res += rec(ne, rest - 1)
        return res

    return rec(start, n)


# O(3^N) -- time
# O(N) -- space

# Exp time without cache.


def knights_dialer_rec_cache(start, n):
    cache = {}

    def rec(curr, rest):
        if (curr, rest) in cache:
            return cache[(curr, rest)]
        if rest == 0:
            return 1
        res = 0
        for ne in ns(curr):
            res += rec(ne, rest - 1)
        cache[(curr, rest)] = res
        return res

    return rec(start, n)


# O(N) -- time
# O(N) -- space

# Still recursive. Stack problem. Plus non-constant space.


def knights_dialer_dynamic(start, n):
    prev = [1] * 10
    curr = [0] * 10
    curr_n = 0

    while curr_n < n:
        curr = [0] * 10
        curr_n += 1

        for i in range(0, 10):
            for ne in ns(i):
                curr[i] += prev[ne]
        prev = curr

    return curr[start]

# O(N) -- time
# O(1) -- space
