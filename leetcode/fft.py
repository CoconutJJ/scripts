import math


def roots_of_unity(n: int) -> list[complex]:

    return [complex(math.cos(2 * math.pi / r), math.sin(2 * math.pi / r))
            for r in range(n, 0, -1)]


def fft(A: list[int]) -> list[complex]:

    if len(A) == 1:
        return [A[0]]

    w = roots_of_unity(len(A))

    odd = []

    even = []

    for (i, v) in enumerate(A):

        if i % 2 == 0:
            even.append(v)
        else:
            odd.append(v)

    odd_eval = fft(odd)
    even_eval = fft(even)

    y = [0 for i in range(len(A))]

    for i in range(0, len(A) // 2):

        y[i] = even_eval[i] + w[i] * odd_eval[i]

        y[i + len(A) // 2] = even_eval[i] - w[i] * odd_eval[i]

    return y


print(fft([0, 1, 2, 3, 4, 5, 6, 7]))
