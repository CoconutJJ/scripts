from collections import defaultdict


def stoneGame(L):

    dp = [float('-inf') for i in range(len(L))]

    for i in range(len(L) - 1, -1, -1):
        take = 0

        j = 0

        while j + i < len(L) and j < 3:

            take += L[i + j]

            dp[i] = max(dp[i], take - dp[i + j + 1])

    if dp[0] > 0:
        return "Alice"

    if dp[0] < 0:
        return "Bob"

    return "Tie"


print(stoneGame([9, -4, 0, 12, -5, -13, 15, 6, -16, 8, 2,
                 16, 12, -6, 13, 0, -16, -11, 9, -14, 7, -1, 14]))
