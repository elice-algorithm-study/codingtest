def solution(n):
    s = '수박'
    answer = ''

    for i in range(n):
        if i % 2 == 0:
            answer += s[0]
        else:
            answer += s[1]

    return answer