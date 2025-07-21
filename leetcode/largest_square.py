def largest_square(L: list[list[int]]):

    mem = dict()

    def rec(i, j):

        if (i, j) not in mem:
            if i == len(L) or j == len(L[0]):
                mem[(i, j)] = 0

            elif L[i][j] == 1:
                mem[(i, j)] = 1 + min(rec(i + 1, j), rec(i, j + 1), rec(i + 1, j + 1))

            else:
                rec(i + 1, j)
                rec(i, j + 1)
                rec(i + 1, j + 1)
                mem[(i, j)] = 0

        return mem[(i, j)]

    rec(0, 0)

    return max(mem[key] for key in mem)    


print(largest_square([[1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1]]))
