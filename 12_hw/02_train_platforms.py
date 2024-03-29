# There is an array of pairs of integers
# where each pair represents train arrival and departure time.
# Write a function that takes the array
# and returns the minimum number of platform that is required
# not to overlap train stops.
#
# Example
# Input: [(900, 910), (940, 1200), (950, 1120), (1100, 1130), (1500, 1900), (1800, 2000)]
# Output: 3


def train_platforms(times):
    arr = sorted(map(lambda el: el[0], times))
    dep = sorted(map(lambda el: el[1], times))
    i, j = 0, 0
    result = 0
    plt_needed = 0
    while j < len(dep):
        if arr[i] < dep[j]:
            plt_needed += 1
            result = max(result, plt_needed)
            i += 1
        else:
            plt_needed -= 1
            j += 1

    return result

# O(NlogN) -- time
# O(N) -- space
