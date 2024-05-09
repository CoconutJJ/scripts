import numpy as np
import sys

calls = 0


def possibleValues(i, j, grid):

    global calls

    calls += 1

    values = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for r in range(9):

        if grid[r][j] in values:
            values.remove(grid[r][j])

        if grid[i][r] in values:
            values.remove(grid[i][r])

    subi, subj = (i // 3) * 3, (j // 3) * 3

    for si in range(subi, subi + 3):
        for sj in range(subj, subj + 3):

            if grid[si][sj] in values:
                values.remove(grid[si][sj])

    return values


def solve(grid):

    idx = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 0:
                idx = (i, j)
                break

        if idx is not None:
            break

    if idx is None:
        return True

    values = possibleValues(idx[0], idx[1], grid)
    for v in values:

        grid[idx[0]][idx[1]] = v

        if solve(grid):
            return True

        grid[idx[0]][idx[1]] = 0

    return False


def parseFile(filename):

    f = open(filename, "r")
    grid = []
    for line in f.readlines():
        line = line.strip("\n").split(" ")
        line = list(map(lambda x: int(x), line))
        grid.append(line)
    return grid


if __name__ == "__main__":

    grid = parseFile(sys.argv[1])

    solve(grid)

    print(np.matrix(grid), "calls = " + str(calls))
