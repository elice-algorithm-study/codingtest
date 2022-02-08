def solution(a, b):
    answer = []

    if a > b:
        for i in range(b, a + 1):
            answer.append(i)
    elif a < b:
        for i in range(a, b + 1):
            answer.append(i)
    else:
        answer.append(a)

    return sum(answer)