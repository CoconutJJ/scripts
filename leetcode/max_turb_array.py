

def computeTurb(A, even_k):
    max_len = 0

    curr_len = 0

    for k in range(len(A) - 1):

        if (k % 2 == 0 if even_k else k % 2 != 0):
            if A[k] > A[k + 1]:
                curr_len += 1
            else:
                if curr_len + 1 > max_len:
                    max_len = curr_len + 1

                curr_len = 0
        else:

            if A[k] < A[k + 1]:
                curr_len += 1
            else:
                if curr_len + 1 > max_len:
                    max_len = curr_len + 1

                curr_len = 0

    if curr_len + 1 > max_len:
        max_len = curr_len + 1

    return max_len


def maxTurbulenceSize(A):

    return max(computeTurb(A, True), computeTurb(A, False))


print(maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
