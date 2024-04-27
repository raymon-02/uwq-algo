# Write a function that takes a string consisting of parenthesis
# and returns the longest substring consisting of balanced parenthesis.
#
# Example
# Input: "(())()(()()))((())"
# Output: 12


def longest_balanced_substring_stack_iter(string):
    stack = []
    cons = []
    for i, char in enumerate(string):
        if char == "(":
            stack.append(i)
        else:
            if stack:
                l = stack.pop()
                while cons and cons[-1][0] > l:
                    cons.pop()
                cons.append((l, i))

    result = 0
    curr_l, curr_r = 0, -1
    for i, (l, r) in enumerate(cons):
        if curr_r + 1 < l:
            result = max(result, curr_r - curr_l + 1)
            curr_l, curr_r = l, r
        elif curr_r + 1 == l:
            curr_r = r
    result = max(result, curr_r - curr_l + 1)

    return result


# O(N) -- time
# O(N) -- space


def longest_balanced_substring_stack(string):
    stack = [-1]
    result = 0
    for i, char in enumerate(string):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                result = max(result, i - stack[-1])
            else:
                stack.append(i)

    return result


# O(N) -- time
# O(N) -- space


def longest_balanced_substring(string):
    def count(reverse=False):
        result = 0
        s = reversed(string) if reverse else string
        open_counter, close_counter = 0, 0
        for char in s:
            if char == "(":
                open_counter += 1
            else:
                close_counter += 1
            if open_counter == close_counter:
                result = max(result, open_counter * 2)
            elif close_counter > open_counter and not reverse or open_counter > close_counter and reverse:
                open_counter, close_counter = 0, 0
        return result

    return max(count(), count(reverse=True))

# O(N) -- time
# O(1) -- space
