

def css(L, k):

    sumToHere = dict()
    sumIndex = dict()
    sumIndex[0] = 0
    sums = set([0])
    currSum = 0

    for i in range(len(L)):
        currSum += L[i]

        sumToHere[i] = currSum
        sumIndex[currSum] = i
        sums.add(currSum)

    for i in range(len(L)):

        currK = k

        while currK <= sumToHere[i]:

            if (N := (sumToHere[i] - currK)
                ) in sums and (i - sumIndex[N] + 1) - 1 >= 2:
                print(sumToHere[i], currK)
                return True
            currK += k

    return False


print(css([2, 6, 4, 7], 6))
