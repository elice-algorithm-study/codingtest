def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        for j in list(range(1, i + 1)):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


print(solution(13, 17))
print(solution(24, 27))
