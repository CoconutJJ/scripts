def solution(xs):

    zcount = 0
    negative_count = 0
    min_abs_neg = float('-inf')
    prod = 1
    for r in xs:

        if r == 0:
            zcount += 1
            continue

        if r < 0:
            negative_count += 1
            min_abs_neg = max(min_abs_neg, r)

        prod = prod * r

    if zcount == len(xs):
        return str(0)

    if negative_count % 2 != 0:

        if negative_count == 1 and negative_count + zcount == len(xs) and zcount > 0:
            return str(0)
        elif negative_count == 1 and len(xs) == 1:
            return str(xs[0])
        else:
            prod = prod / min_abs_neg

    return str(int(prod))


print(solution([-1, -2, -3, 3]))
