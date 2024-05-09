def matrixBlockSum(mat, K):

    def idx(i, j):

        return i * len(mat[j]) + j

    prefixSum = dict()
    prefixSum[0] = mat[0][0]

    currSum = 0

    for i in range(1, len(mat)):

        prefixSum[idx(i, 0)] = prefixSum[idx(i - 1, 0)] + mat[i][0]

    for j in range(1, len(mat[0])):
        prefixSum[idx(0, j)] = prefixSum[idx(0, j - 1)] + mat[0][j]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):
            prefixSum[idx(i, j)] = prefixSum[idx(i - 1, j)] + \
                prefixSum[idx(i, j - 1)] - prefixSum[idx(i - 1, j - 1)]

    answer = [[0 for c in range(len(mat[r]))] for r in range(len(mat))]

    for r in range(len(mat)):
        for c in range(len(mat[r])):

            answer[r][c] = prefixSum[idx(r + K,
                                         c + K)] - prefixSum[idx(r - K,
                                                                 c + K)] - prefixSum[idx(r + K,
                                                                                         c - K)] + prefixSum[idx(r - K,
                                                                                                                 c - K)]

    return answer


print(matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
