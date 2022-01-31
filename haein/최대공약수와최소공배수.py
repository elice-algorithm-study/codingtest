def solution(n, m):
    answer = []
    num = []
    a = n
    b = m
    i = 2
    while i <= min(n, m):
        count = 0
        
        if (n%i == 0 and m%i == 0):
            count += 1
            num.append(i)
            n = n/i
            m = m/i
            i = 2
        else:
            i += 1
    sum1 = 1; 
    for i in num:
        sum1 = sum1 * i
    sum2 = a*b//sum1
    
    answer = [sum1, sum2]
    return answer