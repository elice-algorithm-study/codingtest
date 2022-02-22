def solution(N, stages):
    answer = {}

    for i in range(1, N + 1):  # 1~5 스테이지
        passUser = len([j for j in stages if j >= i])
        if stages.count(i) / passUser == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i) / passUser # 실패율 계산

    return list(sorted(answer, reverse=True, key=lambda x: answer[x]))