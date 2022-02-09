def solution(d, budget):
    answer = 0

    d = sorted(d) # 최소값 차례대로 빼기 위해 정렬

    for i in range(len(d)):
        if budget < d[i]:
            break
        budget -= d[i]
        answer += 1

    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))