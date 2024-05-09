total = 0
perms = set()


def numTilePossibilities(tiles):

    uniq_tiles = {}
    for c in tiles:
        if c not in uniq_tiles:
            uniq_tiles[c] = 1
        else:
            uniq_tiles[c] += 1

    def getPossibilities(currSeq, uniqTiles):

        for c in uniqTiles:

            if uniqTiles[c] != 0 and (currSeq + c) not in perms:

                uniqTiles[c] -= 1

                global total

                total += 1

                perms.add(currSeq + c)

                getPossibilities(currSeq + c, dict(uniqTiles))

                uniqTiles[c] += 1

    getPossibilities("", uniq_tiles)

    return total


def isCoord(grid, c):

    return (0 <= c[0] < len(grid)) and (0 <= c[1] < len(grid[0]))


def uniquePathsIII(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    walkable_square_count = len(grid) * len(grid[0])
    start_coord = None

    for i in range(len(grid)):

        for j in range(len(grid[i])):

            if grid[i][j] == -1:
                walkable_square_count -= 1

            if grid[i][j] == 1:
                start_coord = (i, j)

    visited = [set([start_coord])]

    path = [start_coord]

    visit_count = [1]

    total = 0

    while len(path) != 0:

        step = path.pop(0)

        already_visited = visited.pop(0)

        path_len = visit_count.pop(0)

        if grid[step[0]][step[1]] == -1:
            continue

        if grid[step[0]][step[1]] == 2 and (path_len == walkable_square_count):
            total += 1
            continue

        possible_steps = [
            (step[0] + 1, step[1]),
            (step[0] - 1, step[1]),
            (step[0], step[1] + 1),
            (step[0], step[1] - 1)
        ]

        for p in possible_steps:

            if p not in already_visited and isCoord(grid, p):
                path_set = already_visited.copy()

                path_set.add(p)

                visited.append(path_set)

                path.append(p)

                visit_count.append(path_len + 1)

    return total


def maxScoreWords(words, letters, score):

    max_score = 0
    letter_hash = {}
    for l in letters:

        if l in letter_hash:
            letter_hash[l] += 1
        else:
            letter_hash[l] = 1

    for i in range(2**len(words)):

        curr_score = 0
        curr_letters = dict(letter_hash)

        isValidSet = True

        wordSet = []
        for j in range(len(words)):

            if i & (1 << j) > 0:

                for w in words[j]:

                    if w not in curr_letters:
                        isValidSet = False
                        break

                    curr_letters[w] -= 1

                    if curr_letters[w] < 0:
                        isValidSet = False
                        break

                    curr_score += score[ord(w) - 96 - 1]

            if not isValidSet:
                break

        if (curr_score > max_score) and isValidSet:
            print(wordSet)
            max_score = curr_score

    return max_score


def minAddToMakeValid(S):

    count = 0

    add = 0

    for c in S:

        if c == "(":
            count += 1
        elif c == ")":
            count -= 1

        if count < 0:

            add += 1
            count = 0

    if count > 0:

        add += count

    return add


print(minAddToMakeValid("()))(("))
