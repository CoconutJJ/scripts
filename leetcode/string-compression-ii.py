def optimalCompressionLen(S: str, k: int):
    # 1. Convert S into run-length encoding version via tuples (char, freq)
    encoding = []
    curr = (S[0], 0)

    for c in S:
        s, n = curr
        if c == s:
            curr = (s, n + 1)
        else:
            encoding.append(curr)
            curr = (c, 1)

    encoding.append(curr)

    mem = dict()

    def encodelen(prevCount, prevChar, s, c):
        """
            This function determines the delta between the current length of the
            encoding and the length after add (s,c) to the encoding. It
            automatically adjusts the delta if the current char can merge with the
            previous one.
        """
        if prevChar == s:
            # this means we can merge the current one to the previous encoding
            # tuple
            prevLen = prevCount if prevCount <= 1 else len(
                prevChar + str(prevCount))

            currLen = c + prevCount if c + \
                prevCount <= 1 else len(s + str(c + prevCount))

            return currLen - prevLen
        else:
            # calculate as normal
            if c <= 1:
                return c

            return len(s + str(c))

    def optimalCompRec(prevCount, prevChar, i, k):

        # if we are at the end, no further encoding possible.
        if i == len(encoding):
            return 0

        if (prevCount, prevChar, i, k) not in mem:

            s, c = encoding[i]

            # if cannot delete any more characters, we just sum up everything
            # left
            if k == 0:
                mem[(prevCount, prevChar, i, k)] = encodelen(prevCount, prevChar, s, c) + \
                    optimalCompRec(c if s != prevChar else c + prevCount, s, i + 1, k)

            else:
                minL = float('inf')

                # try deleting as many chars as we can, and find the
                # configuration with minimum length
                for d in range(min(c, k) + 1):

                    p = None

                    if c - d == 0:

                        # if we delete all occurences of this character, then we
                        # pass in our previous char and not the current one.
                        # since it is possible the one before this char and the
                        # next one will merge. eg. "aaabbaaa", k = 2: we can
                        # delete the 2 b's giving us the encoding "a6"

                        p = optimalCompRec(prevCount, prevChar, i + 1, k - d)
                    else:

                        # all other cases, we pass in the current char as the
                        # new previous char.
                        p = encodelen(prevCount, prevChar, s, c - d) + optimalCompRec(
                            c - d + (0 if s != prevChar else prevCount), s, i + 1, k - d)

                    minL = min(minL, p)

                mem[(prevCount, prevChar, i, k)] = minL

        return mem[(prevCount, prevChar, i, k)]

    return optimalCompRec(0, "", 0, k)
