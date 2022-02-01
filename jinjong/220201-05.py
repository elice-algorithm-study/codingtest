def solution(n):
    str_n = str(n)
    answer = 0
    for num in str_n:
        answer += int(num)
    return answer
