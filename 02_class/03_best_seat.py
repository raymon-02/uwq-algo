# You walk into a theatre and you're allowed to sit anywhere within the given row.
# You'd like to sit in the seat that gives you the most space.
# E.g. if there are three empty seats in a row,
# you would prefer to sit in the middle of those three seats.
# If there are no empty seats return -1.
# If there are two equally good seats return seat with the lowest index.
#
# As an input you have a non-empty array containing 0 and 1
# where 0 represents empty seat and 1 represents occupied seat.


import math


def best_seat(seats):
    max_r = 0
    rr = 0
    curr = 0
    ri = 0
    for i, seat in enumerate(seats):
        if seat == 1:
            if max_r < curr:
                max_r = curr
                rr = ri
            curr = 0
        else:
            if curr == 0:
                ri = i
            curr += 1
    if max_r < curr:
        max_r = curr
        rr = ri

    return rr + math.ceil(max_r / 2) - 1

# O(N) -- time
# O(1) -- space
