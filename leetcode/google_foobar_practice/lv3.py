# Fortunately, now that you're Commander Lambda's personal assistant, she's
# confided to you that she made all the access codes "lucky triples" in order to
# help her better find them in the lists. A "lucky triple" is a tuple (x, y, z)
# where x divides y and y divides z, such as (1, 2, 4). With that information,
# you can figure out which list contains the number of access codes that matches
# the number of locks on the door when you're ready to go in (for example, if
# there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access
# codes).

# Write a function answer(l) that takes a list of positive integers l and counts
# the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k. The
# length of l is between 2 and 2000 inclusive. The elements of l are between 1
# and 999999 inclusive. The answer fits within a signed 32-bit integer. Some of
# the lists are purposely generated without any access codes to throw off spies,
# so if no triples are found, return 0.


import math


def answer(l):

    encountered = set()

    L = []

    for c in l:
        if c not in encountered:
            L.append(c)
        encountered.add(c)

    total_count = 0
    for j in range(1, len(L) - 1):

        x_count = 0
        z_count = 0
        for i in range(0, j):
            if L[j] % L[i] == 0:
                x_count += 1

        for k in range(j + 1, len(L)):
            if L[k] % L[j] == 0:
                z_count += 1

        total_count += x_count * z_count
    return total_count

# print(answer([1,5,2,3,5,6,4,34,5,67,45,54,3,23,27,4,3,2,12,2,4,54,56,4,3,2,8,9,8,7,6,5]))


def staircase(N):
    mem = dict()

    def full_staircase(N, m):

        if N == 0:
            return 1

        if m >= N:
            return 0

        total = 0
        for i in range(m + 1, N + 1):

            if (N - i, i) not in mem:
                mem[(N-i, i)] = full_staircase(N-i, i)

            total += mem[(N-i, i)]

        return total

    return full_staircase(N, 0) - 1


print(staircase(200))
