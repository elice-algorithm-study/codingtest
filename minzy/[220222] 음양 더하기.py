def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == 1:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * (-1)

    return answer
