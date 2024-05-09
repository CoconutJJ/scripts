
def maxDistance(L):

    start = None

    maxContZero = 0
    maxStart = None
    for i in range(len(L)):

        if L[i] != 0:

            if start is not None and (i - 1) - start + 1 > maxContZero:
                maxContZero = (i - 1) - start + 1
                maxStart = start

            start = None
        else:

            if start is None:
                start = i

    if start is not None and (len(L) - 1) - start + 1 > maxContZero:
        maxContZero = (len(L) - 1) - start + 1
        maxStart = start

    return maxStart + maxContZero // 2 + 1


print(maxDistance([1, 0, 0, 0, 1, 0, 1]))
