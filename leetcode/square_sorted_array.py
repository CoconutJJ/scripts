def sortedSquares(A):

    pos = []
    neg = []

    lo = 0
    hi = len(A)

    while lo < hi:

        i = (lo + hi) // 2
        # print(lo, hi)
        if A[i] < 0:
            lo = i + 1
        elif A[i] > 0:
            hi = i - 1
        else:
            pos = A[i:]
            neg = A[:i]
            break

    if len(pos) == len(neg) == 0:

        if A[lo] < 0:
            pos = A[lo + 1:]
            neg = A[:lo + 1]
        else:
            neg = A[:lo]
            pos = A[lo:]

    neg.reverse()
    sorted_arr = []

    pos_i = 0
    neg_j = 0

    while pos_i < len(pos) and neg_j < len(neg):

        if pos[pos_i]**2 > neg[neg_j]**2:
            sorted_arr.append(neg[neg_j]**2)
            neg_j += 1
        else:
            sorted_arr.append(pos[pos_i]**2)
            pos_i += 1

    if len(pos[pos_i:]) == 0:
        sorted_arr = sorted_arr + [n**2 for n in neg[neg_j:]]
    else:

        sorted_arr = sorted_arr + [n**2 for n in pos[pos_i:]]

    return sorted_arr


print(sortedSquares([-4, -1, 0, 3, 10]))
