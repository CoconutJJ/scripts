def getZeroIndex(L):

    i = 0
    j = len(L) - 1

    if L[-1] < 0 or L[0] >= 0:
        return -1

    while i < j:

        mid = (i + j) // 2

        if L[mid] >= 0 and L[mid - 1] < 0:
            return mid

        if L[mid] < 0:
            i = mid
        else:
            j = mid

    return -1


def maxSatisfaction(satisfaction):

    satisfaction.sort()

    maxSum = 0

    start = getZeroIndex(satisfaction)

    if start == -1 and satisfaction[-1] >= 0:

        for j in range(len(satisfaction)):

            maxSum += satisfaction[j] * (j + 1)

        return maxSum

    currSum = sum([(i - start + 1) * satisfaction[i]
                  for i in range(start, len(satisfaction))])
    incr = sum(satisfaction[start:])

    for i in range(start - 1, -1, -1):
        incr += satisfaction[i]
        currSum += incr

        if currSum < maxSum:
            break
        else:
            maxSum = currSum

    return maxSum
