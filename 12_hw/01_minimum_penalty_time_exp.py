# There is an array of pairs of positive integers
# where each pair represents the amount of time
# that specific task takes to be finished
# and a coefficient for penalty function depending on
# waiting time before this task execution.
# Penalty function is exponential: f_i(t) = c_i * e^t
# where c_i is a coefficient for penalty.
#
# Write a function that takes the array
# and returns the minimum amount of total penalty
# that can be achieved for some order of task execution.
#
# It is allowed to mutate the array.
#
# Example
# Input: [(4, 2), (5, 5), (1, 3)]
# Output: 750.5
# Optimal order of execution is 1, 4, 5.
# Penalty is:
# 3 * e^0 + 2 * e^(0 + 1) + 5 * e^(0 + 1 + 4) = 3 + 2e + 5e^5 =~ 750.5


def minimum_penalty_time_exp(tasks):
    pass
