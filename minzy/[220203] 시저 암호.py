def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = []

    for c in s:
        if c in low:
            answer.append(low[(low.index(c) + n) % 26])
        elif c in up:
            answer.append(up[(up.index(c) + n) % 26])
        else:
            answer.append(' ')

    return ''.join(answer)