import random


def kthSmallest(L, k):

    mid = random.randint(0, len(L) - 1)
    left = [l for i, l in enumerate(L) if l <= L[mid] and mid != i]
    right = [l for i, l in enumerate(L) if l > L[mid] and mid != i]

    if k == len(left) + 1:
        return L[mid]
    elif k < len(left) + 1:
        return kthSmallest(left, k)
    else:
        return kthSmallest(right, k - len(left) - 1)


def median(L):

    if len(L) % 2 == 0:

        return (kthSmallest(L, len(L) // 2) +
                kthSmallest(L, len(L) // 2 + 1)) / 2
    else:
        return kthSmallest(L, len(L) // 2 + 1)


def kWindowMedian(L, k):

    medians = []

    for i in range(0, len(L) - k + 1):
        medians.append(median(L[i: i + k]))

    return medians


print(kWindowMedian([-1, 5, 13, 8, 2, 3, 3, 1], 4))

print(kWindowMedian([1, 2, 3], 3))
