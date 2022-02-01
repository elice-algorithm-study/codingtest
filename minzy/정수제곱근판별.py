def solution(n):
    answer = 0
    chk = n ** (1 / 2)

    if chk == int(chk):
        answer = (chk + 1) ** 2
    else:
        answer = -1

    return answer