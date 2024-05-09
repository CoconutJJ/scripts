
diagonals = set()

rows = set()

cols = set()

perms = 0


def canPlaceQueen(c):

    if c[1] in rows:
        return False

    if c[0] in cols:
        return False

    if ((c[1] - c[0]) in diagonals or (c[1] + c[0]) in diagonals):
        return False

    return True


def nQueen(board, col):

    N = len(board)

    if col >= N:
        return True

    for i in range(N):

        if canPlaceQueen((col, i)):

            board[i][col] = 'Q'

            rows.add(i)
            cols.add(col)
            diagonals.add(i - col)
            diagonals.add(i + col)

            if nQueen(board, col + 1):
                return True

            board[i][col] = '.'
            try:
                rows.remove(i)
                cols.remove(col)
                diagonals.remove(i - col)
                diagonals.remove(i + col)
            except BaseException:
                continue

    return False


board = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
]

# [
#     ['.', '.', '.', '.', '.', '.', 'Q', '.'],
#     ['Q', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', 'Q', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', 'Q'],
#     ['.', '.', '.', '.', '.', 'Q', '.', '.'],
#     ['.', '.', '.', 'Q', '.', '.', '.', '.'],
#     ['.', 'Q', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', 'Q', '.', '.', '.']
# ]

nQueen(board, 0)
