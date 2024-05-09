def numIslands(grid):

    def inGrid(c):

        return (c[0] < len(grid)) and (c[1] < len(grid[0]))

    q = [(0, 0)]

    islandCount = 0

    # marks the island as attached, do not count.
    markAttached = set()

    while len(q) != 0:

        c = q.pop(0)

        ci, cj = c  # tuple unpacking

        # right and bottom neighbour
        neighbours = [(c[0], c[1] + 1), (c[0] + 1, c[1])]

        # check if it is "water", if so just push neighbours in and continue
        if grid[ci][cj] != '1':

            for n in neighbours:

                if inGrid(n):
                    q.append(n)

            continue

        # if this "land" has not been accounted for then increase island count
        if c not in markAttached:
            islandCount += 1
            # mark this island as attached
            markAttached.add(c)

        # go through the neighbours
        for n in neighbours:

            (i, j) = n

            if inGrid(n):

                # if the neighbour is a 1, mark those as attached.
                if grid[i][j] == '1':
                    markAttached.add(n)

                # push into q.
                q.append(n)

    return islandCount


print(numIslands([
    ['0', '1'],
    ['1', '1']
]))
