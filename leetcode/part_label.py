def partition(S):

    freq = dict()

    for c in S:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    runningSet = set()
    currPart = ""
    parts = []
    for c in S:
        runningSet.add(c)
        freq[c] -= 1
        currPart += c

        if freq[c] == 0:
            runningSet.remove(c)

            if len(runningSet) == 0:

                parts.append(currPart)
                currPart = ""

    return parts


print(partition("ababcbacadefegdehijhklij"))
