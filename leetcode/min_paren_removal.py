
def min_paren_removal(s: str):

    count = 0
    removals = 0
    for c in s:

        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

            if count < 0:
                removals += 1
                count = 0

    return removals + count


if __name__ == "__main__":

    assert min_paren_removal("()()())") == 1
    assert min_paren_removal("((((()") == 4
    assert min_paren_removal("(((()))))))") == 3
    assert min_paren_removal("()()())())") == 2
    assert min_paren_removal(")(") == 2
