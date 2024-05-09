import heapq


def minNumberOperations(target):

    curr_max = 0

    ops = 0

    for c in target:

        if c > curr_max:
            ops += c - curr_max

        curr_max = c

    return ops


print(minNumberOperations([3, 1, 1, 2]))
