# Write a function that takes text
# and returns a table with chars
# decoded by Huffman algorithm.
#
# Example
# Input: "aaaabbbbcccdddeefg"
# Output: {"a":"00", "b": "01", "c":"110", "d": "111", "e": "100", "f": "1010", "g": "1011"}


class Node:
    def __init__(self, count, ch=None, left=None, right=None):
        self.count = count
        self.ch = ch
        self.left = left
        self.right = right


def huffman_algo(text):
    root = huffman_algo_root(text)
    result = {}

    def rec(node, path):
        if not node.left and not node.right:
            result[node.ch] = "".join(path)
            return
        path.append("0")
        rec(node.left, path)
        path.pop()
        path.append("1")
        rec(node.right, path)
        path.pop()

    rec(root, [])
    return result


def huffman_algo_root(text):
    if not text:
        return {}

    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1
    cch = [Node(count, ch=ch) for ch, count in frequency.items()]

    if len(cch) == 1:
        return {cch[0].ch: "0"}

    cch.sort(key=lambda el: el.count)
    root = Node(
        cch[0].count + cch[1].count,
        ch=cch[0].ch + cch[1].ch,
        left=Node(cch[0].count, ch=cch[0].ch),
        right=Node(cch[1].count, ch=cch[1].ch)
    )
    sum_arr = [root]
    i, j = 2, 0
    while i < len(cch):
        if cch[i].count <= sum_arr[j].count:
            if i + 1 < len(cch) and cch[i + 1].count <= sum_arr[j].count:
                sum_arr.append(
                    Node(
                        cch[i].count + cch[i + 1].count,
                        ch=cch[i].ch + cch[i + 1].ch,
                        left=cch[i],
                        right=cch[i + 1]
                    )
                )
                i += 2
            else:
                sum_arr.append(
                    Node(
                        cch[i].count + sum_arr[j].count,
                        ch=cch[i].ch + sum_arr[j].ch,
                        left=cch[i],
                        right=sum_arr[j]
                    )
                )
                i += 1
                j += 1
        else:
            if j + 1 < len(sum_arr) and sum_arr[j + 1].count < cch[i].count:
                sum_arr.append(
                    Node(
                        sum_arr[j].count + sum_arr[j + 1].count,
                        ch=sum_arr[j].ch + sum_arr[j + 1].ch,
                        left=sum_arr[j],
                        right=sum_arr[j + 1]
                    )
                )
                j += 2
            else:
                sum_arr.append(
                    Node(
                        sum_arr[j].count + cch[i].count,
                        ch=sum_arr[j].ch + cch[i].ch,
                        left=sum_arr[j],
                        right=cch[i]
                    )
                )
                i += 1
                j += 1

    while j + 1 < len(sum_arr):
        sum_arr.append(
            Node(
                sum_arr[j].count + sum_arr[j + 1].count,
                ch=sum_arr[j].ch + sum_arr[j + 1].ch,
                left=sum_arr[j],
                right=sum_arr[j + 1]
            )
        )
        j += 2

    return sum_arr[-1]

# O(NlogN) -- time
# O(N) -- space
