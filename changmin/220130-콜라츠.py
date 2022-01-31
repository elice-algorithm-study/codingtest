def solution(num):
    answer = 0
    n = num
    if num == 1 : return 0
    while 1:
        
        n = n/2 if n % 2 == 0 else (n*3)+1
        answer += 1

        if n == 1: return answer
        elif answer == 500: return -1       
            
    return answer