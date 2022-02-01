import math
def solution(n):
    s = math.sqrt(n)
    
    if int(s) == s:
        return (s + 1) **2

    else: return -1