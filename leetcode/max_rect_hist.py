def maxRectHist(L):

    heights = [L[0]]
    pos = [0]

    max_area = 0

    for i in range(1, len(L)):

        top = heights[-1]

        if L[i] > top:
            heights.append(L[i])
            pos.append(i)

            max_area = max(max_area, L[i])
        else:
            curr_pos = None

            while heights[-1] >= top:
                heights.pop()
                curr_pos = pos.pop()

            max_area = max(max_area, (i - curr_pos + 1) * top)

            pos.append(curr_pos)
            heights.append(top)

    while len(heights) > 0:

        h = heights.pop()
        curr_pos = pos.pop()

        max_area = max(max_area, ((len(L) - 1) - curr_pos + 1) * h)

    return max_area


print(maxRectHist([1, 2, 3, 4, 5]))
