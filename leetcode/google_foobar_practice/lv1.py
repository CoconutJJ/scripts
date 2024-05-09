# Write a function called answer(data, n) that takes in a list of less than 100
# integers and a number n, and returns that same list but with all of the
# numbers that occur more than n times removed entirely. The returned list
# should retain the same ordering as the original list - you don't want to mix
# up those carefully planned shift rotations! For instance, if data was [5, 10,
# 15, 10, 7] and n was 1, answer(data, n ) would return the list [5, 15, 7]
# because 10 occurs twice, and was thus removed from the list entirely.

def answer(L, n):

    count = dict()

    for c in L:

        if c not in count:
            count[c] = 1
            continue

        count[c] += 1

    filtered = []

    for c in L:

        if count[c] <= n:
            filtered.append(c)

    return filtered


print(answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
