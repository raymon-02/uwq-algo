# Write a function that takes string of digits
# and returns all possible mnemonics
# associated with keypad of mobile phone.
#
# Each button of keypad contains digit and letters like:
# 1 has no letters
# 2 has 'a', 'b', 'c'
# 3 has 'd', 'e', 'f'
# 4 has 'g', 'h', 'i'
# 5 has 'j', 'k', 'l'
# 6 has 'm', 'n', 'o'
# 7 has 'p', 'q', 'r', 's'
# 8 has 't', 'u', 'v'
# 9 has 'w', 'x', 'y', 'z'
# 0 has no letters
#
# So input string "234" can be presented
# like "aei" or "bfg" or "cdh" and so on.
#
# If digit has no letters then it should be presented as is.
#
# Example
# Input: "290"
# Output: ["aw0", "ax0", "ay0", "az0", "bw0", "bx0", "by0", "bz0", "cw0", "cx0", "cy0", "cz0"]


def dialer_mnemonics(s):
    keys = {
        "0": "0",
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []

    def rec(i, path):
        if i == len(s):
            result.append("".join(path))
            return
        for l in keys[s[i]]:
            path.append(l)
            rec(i + 1, path)
            path.pop()

    rec(0, [])

    return result

# O(N * 4^N) -- time
# O(N * 4^N) -- space
