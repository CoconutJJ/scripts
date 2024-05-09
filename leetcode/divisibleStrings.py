

def divisibleStrings(s, t):

    if len(s) % len(t) != 0:
        return -1

    if s != (t * (len(s) // len(t))):
        return -1

    for i in range(len(s)):

        if t[i % len(s)] != s[0] or i == 0:
            continue
        j = 0

        while j < len(t):

            if t[j % i] != t[j]:
                break
            j += 1

        if j == len(s):
            return i

    return -1


print(divisibleStrings("abcdabcdabcdabcdabcd", "abcd"))
