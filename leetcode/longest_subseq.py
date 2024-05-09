
def longestSubsequence(A, B):
    mem = dict()

    def LSRec(i, j):

        if i == len(A):
            return 0
        if j == len(B):
            return 0

        if (i, j) not in mem:

            if A[i] == B[j]:
                mem[(i, j)] = max(1 + LSRec(i + 1, j + 1),
                                  LSRec(i, j + 1), LSRec(i + 1, j))
            else:
                mem[(i, j)] = max(LSRec(i + 1, j + 1),
                                  LSRec(i, j + 1), LSRec(i + 1, j))

        return mem[(i, j)]

    return LSRec(0, 0)


print(longestSubsequence("AGGTAB", "GXTXAYB"))
