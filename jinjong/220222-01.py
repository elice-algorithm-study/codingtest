from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num//2+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_set = set()
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            word = ''.join(j)
            num_set.add(int(word))

    for num in num_set:
        if isPrime(num):
            answer += 1
            
    return answer
