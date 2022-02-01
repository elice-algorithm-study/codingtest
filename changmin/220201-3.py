def solution(n): 
    
    a = list(str(n))
    a.reverse()
    a = [int(x) for x in a]
    return a

print(solution(12345))