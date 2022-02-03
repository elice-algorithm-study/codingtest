def solution(n):
    answer = 0
    
    for i in range(1, n+1, 2):
        if i == 1:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else: 
            answer += 1
    
    answer += 1
    
    return answer