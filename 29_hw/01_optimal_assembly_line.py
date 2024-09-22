# Write a function that takes
# an array of positive integers representing step durations
# and positive integer representing number of stations
# and returns the longest duration of a single station
# in optimized assembly process.
#
# Each station can perform multiple consecutive steps.
# When one station finishes the next one performs several consecutive steps.
# In the end all steps should be performed.
# The duration of one station is a sum of step durations that this station performs.
# Optimized assembly process means that duration of each station is as short as possible.
#
# Example
# Input: [15, 15, 30, 30, 45], 3
# Output: 60
# The first station performs steps 0 and 1.  Duration is 15 + 15 = 30
# The second station performs steps 2 and 3. Duration is 30 + 30 = 60
# The third station performs step 4.         Duration is 45
# The longest duration across stations is 60.
# Assembly process is optimized since 60 is the shortest duration
# among all possible step distributions across stations.
# E.g. the first station can perform step 0 only.
# But it leads that some other station has to perform more steps and increase its duration.


def optimal_assembly_line(durations, stations):
    pass
