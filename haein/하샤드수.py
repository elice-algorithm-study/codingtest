def solution(x):
    answer = True
    num = str(x)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    
    if x % sum != 0: answer = False
    
    return answer