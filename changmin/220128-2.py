def solution(x, n):
    answer = []
    a = 0
    for i in range(n):        
        answer.append(x + a)
        a += x
        
    return answer