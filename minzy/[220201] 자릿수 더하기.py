def solution(n):
    answer = 0
    n_list = list(map(int, str(n)))

    for i in n_list:
        answer += i

    return answer