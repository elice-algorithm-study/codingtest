def solution(s):
    up, low = [], []
    for c in s:
        if c.isupper():
            up.append(c)
        else:
            low.append(c)

    return ''.join(sorted(low, reverse=True) + sorted(up, reverse=True))