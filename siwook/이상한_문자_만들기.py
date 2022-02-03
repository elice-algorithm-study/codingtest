def solution(s):
    answer = ''
    s = list(s)
    j = 0
    for i in s:
        if i != ' ':            
            if j % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            j += 1
        else:
            answer += ' '
            j = 0

    return answer
