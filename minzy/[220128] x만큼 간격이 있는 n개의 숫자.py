def solution(x, n):
    answer = []
    c = x

    for _ in range(0, n):
        answer.append(c)
        c += x

    return answer