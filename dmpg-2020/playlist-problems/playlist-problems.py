a = input()
b = input()


def diff(a, b):
    '''
    Procedure: 
    1. Find and remove characters in the correct positions
    2. Find and remove characters in incorrect positions
    3. Find and remove characters in A not in B
    4. Add the absolute difference
    '''

    a, b = map(list, [a, b])
    score = 0

    # 1.
    for i, c in enumerate(a):
        if b[i] == c:
            score -= 1
            del a[i], b[i]
            print(a, b)

    # 2.
    for i, c in enumerate(a):
        try:
            i_b = b.index(c)
        except:
            pass
        else:
            score -= 0.5
            del b[i_b], a[i]
        print(a, b)

    # 3.
    score += len(a)

    # 4.
    score += abs(len(a) - len(b))

    return score


print(diff(a, b))
