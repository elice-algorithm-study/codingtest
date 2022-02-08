def solution(s):
    p, y = [], []

    s = s.lower()

    for c in s:
        if c == 'p':
            p.append(c)
        elif c == 'y':
            y.append(c)

    if len(p) == len(y):
        return True
    else:
        return False