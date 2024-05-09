

def knapsack(P, W, MAX_WEIGHT):

    PW = list(zip(P, W))

    PW.sort(key=lambda r: r[1])

    PW = [(0, 0)] + PW

    grid = [[-1 for i in range(MAX_WEIGHT + 1)] for i in range(len(PW))]

    def tab(p, w):
        if p < 0 or w < 0:
            return float('-inf')

        if grid[p][w] == -1:

            if p == 0 or w == 0:
                grid[p][w] = 0
            else:

                grid[p][w] = max(
                    tab(p - 1, w), tab(p - 1, w - PW[p][1]) + PW[p][0])

        return grid[p][w]

    maxSum = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = tab(i, j)
            maxSum = max(maxSum, grid[i][j])

    return maxSum
