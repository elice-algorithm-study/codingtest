import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    
    if n >= m:
        n, m = m, n
    
    i = 1
    while True:
        if (math.gcd(n, m) * i) % n == 0 and (math.gcd(n, m) * i) % m == 0:
            answer.append(math.gcd(n, m) * i)
            break
        i += 1
        
    return answer
  
  
"""
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a * b / c)]

    return answer
"""
  
