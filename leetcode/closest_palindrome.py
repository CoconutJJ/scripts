'''
Problem:

A palindrome is a string that spells the same forward and backward.

Given a string S, find the minimum number of characters to remove from S
in order for S to be a palindrome.

e.g

S = ""

closest_palindrome(S) = 0, empty string is considered a palindrome

S = "abcdefghfedcba"

closest_palindrome(S) = 1, remove g or h

S = "fgf"

closest_palindrome(S) = 0, S is already a palindrome

S = "acdea"

closest_palindrome(S) = 2, remove any 2 of c, d and e.
'''


def closest_palindrome_rec(s: str):
    '''
    

    '''

    mem = dict()

    def rec(i, j):

        if (i,j) not in mem:
            if i >= j:
                return 0

            if s[i] == s[j]:
                mem[(i,j)] = rec(i + 1, j - 1)
            else:
                mem[(i,j)] = 1 + min(rec(i + 1, j), rec(i, j - 1))

        return mem[(i,j)]

    return rec(0, len(s) - 1)


def closest_palindrome_iter(s: str):
    '''

    dp[(i,j)] is the minimum number of characters to remove from s[i:j + 1]
    such s[i:j + 1] is a palindrome.

    The bottom-up approach starts from substrings of size 1 up to size N where
    i is the starting index of the substring.

    Base Case: Substring of size 1 has optimal solution of 0.
    Recursive Step: To find all optimal solutions for substrings of size K > 1,
    use solutions stored for size K - 1.
    '''
    dp = dict()

    for N in range(1, len(s) + 1):
        for i in range(0, len(s) - N + 1):

            start, end = i, i + N - 1

            if start == end:
                dp[(start, end)] = 0
                continue

            if s[start] == s[end]:
                dp[(start, end)] = dp[(start + 1, end - 1)]
            else:
                dp[(start, end)] = 1 + \
                    min(dp[(start + 1, end)], dp[(start, end - 1)])

    return dp[(0, len(s) - 1)]


print(closest_palindrome_iter("acdea"))
