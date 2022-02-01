def solution(n):
    answer = 0
    i = 1
    while i < (n/2):
        if (i*i)==n:
            answer = (i+1)*(i+1)
            break
        i+=1
    
    if n==1:
        answer = 4
    return answer if answer!=0 else -1
