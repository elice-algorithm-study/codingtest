def func(num):
    count = 0
    for i in range(1, num//2+1):
        if num%i == 0:
            count += 1
    if (count+1) % 2 == 0:
        return True
    else :
        return False

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if func(i):
            answer += i
        else :
            answer -= i
            
    return answer
