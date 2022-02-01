def solution(n):
    answer = 0
    i = 1
    while i*i <= n:
        if i*i == n:
            answer = i
            break
        else :
            i += 1
    if answer == 0:
        answer = -1
    else :
        answer = (answer + 1) * (answer + 1)
    
    
    return answer