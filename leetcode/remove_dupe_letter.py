
from collections import defaultdict


def remove_duplicate_letters(S):

    freq = defaultdict(0)

    used = set()

    order = []

    for c in S:

        freq[c] += 1

    for c in S:

        freq[c] -= 1

        while len(order) > 0 and freq[order[-1]] > 0 and order[-1] > c:
            order.pop()

        used.add(c)
        order.append(c)

    return "".join(order)
