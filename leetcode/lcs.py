def LongestCommonSubsequence(S, T):
    mem = dict()

    def LCSRec(i, j):

        if i == len(S) or j == len(T):
            return 0

        if (i, j) not in mem:
            if S[i] == T[j]:
                mem[(i, j)] = 1 + LCSRec(i + 1, j + 1)
            else:
                mem[(i, j)] = max(LCSRec(i + 1, j), LCSRec(i, j + 1))

        return mem[(i, j)]

    return LCSRec(0, 0)


def LongestIncreasingSubsequence(L):
    mem = dict()
    L = [float('-inf')] + L

    def LISRec(prev, curr):

        if curr == len(L):
            return 0

        if (prev, curr) not in mem:
            if L[curr] > L[prev]:
                mem[(prev, curr)] = max(
                    1 + LISRec(curr, curr + 1), LISRec(prev, curr + 1))
            else:
                mem[(prev, curr)] = LISRec(prev, curr + 1)

        return mem[(prev, curr)]

    return LISRec(0, 1)


def LongestIncreasingSubsequenceIter(L):
    mem = dict()

    mem[0] = 1

    for curr in range(1, len(L)):
        max_len = 0
        for prev in range(curr):

            if L[curr] > L[prev]:
                max_len = max(max_len, 1 + mem[prev])

        mem[curr] = max_len

    return mem[len(L) - 1]


print(LongestIncreasingSubsequenceIter([1, 2, 3, 4, 5]))
