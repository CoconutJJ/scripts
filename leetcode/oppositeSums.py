
fact = dict()


def rev(n):

    n = str(n)

    digits = [c for c in n]

    digits.reverse()

    return int("".join(digits))


def factr(n):

    if n <= 1:
        return 1

    if n not in fact:
        fact[n] = n * factr(n - 1)

    return fact[n]


def choose(n, k):

    if n < k:
        return 0

    return factr(n) / (factr(k) * factr(n - k))


def oppositeSums(L):

    # arr[i] + rev(arr[j]) = arr[j] + rev(arr[i])

    freq = dict()

    for c in L:

        ind = c - rev(c)
        print(ind)
        if ind not in freq:

            freq[ind] = 1
        else:
            freq[ind] += 1

    count = 0

    for f in freq:

        count += choose(freq[f], 2) + freq[f]

    return count


print(oppositeSums([1, 20, 2, 11, 5, 7, 5, 3]))
