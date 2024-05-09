# Recall.ai Technical Interview 1 - Print all possible ending configurations
# in Tic Tac Toe

visited = set()


def is_ending_configuration(grid: list[list[str]]):

    for row in range(len(grid)):
        r = "".join(grid[row])
        if r == "XXX" or r == "OOO":
            return True

    for col in range(len(grid)):
        c = []
        for i in range(0, 3):
            c.append(grid[i][col])

        cstr = "".join(c)

        if cstr == "XXX" or cstr == "OOO":
            return True

    main_diag = []
    for i in range(0, 3):
        main_diag.append(grid[i][i])

    main_diag_str = "".join(main_diag)

    if main_diag_str == "XXX" or main_diag_str == "OOO":
        return True

    anti_diag = []

    for i in range(0, 3):

        anti_diag.append(grid[i][2 - i])

    anti_diag_str = "".join(anti_diag)

    if anti_diag_str == "XXX" or anti_diag_str == "OOO":
        return True

    for i in range(len(grid)):
        for j in range(len(grid)):

            if grid[i][j] == '.':
                return False

    return True


def tic_tac_toe(grid: list[list[str]], symbol: str):

    if is_ending_configuration(grid):

        serialized = "".join("".join(r) for r in grid)
        if serialized in visited:
            return 0
        else:
            visited.add(serialized)
            return 1

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid)):

            if grid[i][j] == '.':

                grid[i][j] = symbol

                total += tic_tac_toe(grid, 'X' if symbol == 'O' else 'O')

                grid[i][j] = '.'

    return total


print(tic_tac_toe([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], 'X'))
