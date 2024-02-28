# There is an array of positive integers
# where each element represents the amount of time
# that specific task takes to be finished.
#
# Write a function that takes the array
# and returns the minimum amount of total waiting time
# that can be achieved for some order of task execution.
#
# It is allowed to mutate the array.
#
# Example
# Input: [5, 1, 4]
# Output: 5
# Optimal order of execution is 4, 1, 5.
# Waiting time is:
# 0 + (0 + 4) + (0 + 4 + 1) = 5


def minimum_penalty_time_lin_one(tasks):
    tasks.sort()
    result = 0
    wait_time = 0
    for time in tasks:
        result += wait_time
        wait_time += time

    return result


# O(NlogN) -- time
# O(1) -- space


# There is an array of pairs of positive integers
# where each pair represents the amount of time
# that specific task takes to be finished
# and a coefficient that should be multiplied
# by waiting time before this task execution
# to get a penalty amount of this task.
#
# Write a function that takes the array
# and returns the minimum amount of total penalty
# that can be achieved for some order of task execution.
#
# It is allowed to mutate the array.
#
# Example
# Input: [(4, 2), (5, 5), (1, 3)]
# Output: 17
# Optimal order of execution is 1, 5, 4.
# Penalty is:
# 3 * 0 + 5 * (0 + 1) + 2 * (0 + 1 + 5) = 0 + 5 + 12 = 17


# Common case:
# F(p) = f_p1(0) + f_p2(t_p1) + f_p3(t_p1 + t_p2) +...+ f(sum(i=1,n-1)t_pi)
# Let p be the optimal permutation.
# Let p' be some permutation.
#
# f is linear function.
# f_i(t) = c_i * t
# Then
# F(p') - F(p) = c_pi * t_pi+1 - c_pi+1 * t_pi >= 0
# Then
# c_pi/t_pi >= c_pi+1/t_pi+1
# Then
# Need to sort by task[1]/task[0] in reversed order.
def minimum_penalty_time_lin(tasks):
    tasks.sort(key=lambda el: el[1] / el[0], reverse=True)
    result = 0
    wait_time = 0
    for (time, coefficient) in tasks:
        penalty = coefficient * wait_time
        result += penalty
        wait_time += time

    return result

# O(NlogN) -- time
# O(1) -- space
