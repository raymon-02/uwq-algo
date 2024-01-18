# There are n gas stations along a circular route
# where the amount of gas at the station i is gas[i].
# You have a car with an unlimited gas tank.
# It costs cost[i] of gas to travel from the station i to the station i+1.
# You begin with an empty tank at one of the gas stations.
#
# Write a function that takes array of positive integers `gas`,
# array of positive integers `cost`
# and returns the starting gas station's index in case
# when it's possible to travel around the circuit once in the clockwise direction
# Otherwise return -1.
#
# Example
# Input: [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
# Output: 3

def gas_stations(gas, cost):
    tank, deficit, start = 0, 0, 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        tank += g - c
        if tank < 0:
            start = i + 1
            deficit += tank
            tank = 0

    return start if tank + deficit >= 0 else -1

# O(N) -- time
# O(1) -- space
