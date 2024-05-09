from collections import defaultdict


def burstBalloon(L):

    def val(ind):

        if ind == -1 or ind == len(L):

            return 1

        else:

            return L[ind]

    dp = dict()

    def burst(i, j):

        if (i, j) not in dp:

            dp[(i, j)] = 0

            for r in range(i, j + 1):

                dp[(i, j)] = max(

                    dp[(i, j)],

                    val(i - 1) * val(r) * val(j + 1) +
                    burst(i, r - 1) + burst(r + 1, j)

                )

        return dp[(i, j)]

    return burst(0, len(L) - 1)


print(burstBalloon([3, 1, 5, 8]))
