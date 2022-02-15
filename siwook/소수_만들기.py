import math
from itertools import combinations

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0    
    result = list(combinations(nums, 3))
    
    for i in result:
        if is_prime_number(sum(i)) == True:
            answer += 1

    return answer
  
  
"""
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
"""
