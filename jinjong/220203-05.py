import math

def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

def solution(n):
    answer = 0
    arr = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]==True:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j+=1
    for i in range(2, len(arr)):
        if arr[i]: answer +=1
            
    return answer
