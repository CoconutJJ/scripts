# Write a program that counts how many salutes are exchanged during a typical
# walk along a hallway. The hall is represented by a string. For example:
# "--->-><-><-->-"

# Each hallway string will contain three different types of characters: '>', an
# employee walking to the right; '<', an employee walking to the left; and '-',
# an empty space. Every employee walks at the same speed either to right or to
# the left, according to their direction. Whenever two employees cross, each of
# them salutes the other. They then continue walking until they reach the end,
# finally leaving the hallway. In the above example, they salute 10 times.

# Write a function answer(s) which takes a string representing employees walking
# along a hallway and returns the number of times the employees will salute. s
# will contain at least 1 and at most 100 characters, each one of -, >, or <.

def answer(s):

    total_right_facing = 0

    for i in range(len(s)):
        if s[i] == '<':
            total_right_facing += 1

    salutes = 0

    for i in range(len(s)):
        if s[i] == '<':
            total_right_facing -= 1
        elif s[i] == '>':
            salutes += 2*total_right_facing
        else:
            continue

    return salutes


print(answer("--->-><-><-->>-<<->><-<<->>-"))


# Given a non-empty list of positive integers l and a target positive integer t,
# write a function answer(l, t) which verifies if there is at least one
# consecutive sequence of positive integers within the list l (i.e. a contiguous
# sub-list) that can be summed up to the given target positive integer t (the
# key) and returns the lexicographically smallest list containing the smallest
# start and end indexes where this sequence can be found, or returns the array
# [-1, -1] in the case that there is no such sequence (to throw off Lambda's
# spies, not all number broadcasts will contain a coded message).

# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as
# 12, the function answer(l, t) would return the list [0, 2] because the list l
# contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for
# which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens
# later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4]
# and the key t as 15, the function answer(l, t) would return [-1, -1] because
# there is no sub-list of list l that can be summed up to the given target value
# t = 15.

# To help you identify the coded broadcasts, Bunny HQ has agreed to the
# following standards:

# Each list l will contain at least 1 element but never more than 100. Each
# element of l will be between 1 and 100. It will be a positive integer, not
# exceeding 250. The first element of the list l has index 0. For the list
# returned by answer(l, t), the start index must be equal or smaller than the
# end index. Remember, to throw off Lambda's spies, Bunny HQ might include more
# than one contiguous sublist of a number broadcast that can be summed up to the
# key. You know that the message will always be hidden in the first sublist that
# sums up to the key, so answer(l, t) should only return that sublist.

def p2answer(L, t):

    numbers = set()
    sumAt = dict()
    sumTo = dict()
    currSum = 0
    start = end = None

    numbers.add(0)
    sumTo[0] = 0
    for i in range(len(L)):

        currSum += L[i]
        if (currSum - t) in numbers:
            print("found")
            end = i
            start = sumTo[currSum - t]
            break

        sumAt[i] = currSum

        if currSum not in sumTo:
            sumTo[currSum] = i

        numbers.add(currSum)

    return [-1, -1] if start is None and end is None else [start, end]


print(p2answer([1, 2, 3, 4], 12))
