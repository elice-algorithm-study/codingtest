def solution(N, stages):
    answer = {}

    for i in range(1, N + 1):  # 1~5 스테이지
        divisor = len([j for j in stages if j >= i])
        if divisor != 0:
            answer[i] = stages.count(i) / divisor # 실패율 계산
        else:
            answer[i] = 0
    return list(sorted(answer, reverse=True, key=lambda x: answer[x]))
