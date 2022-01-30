def solution(x):
    x = str(x)
    arr = list(x)
    sum = 0
    for i in arr:
        sum += int(i)
    
    if int(x) % sum == 0:
        answer = True
    else:
        answer = False
        
    return answer
  
  
"""
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
"""
