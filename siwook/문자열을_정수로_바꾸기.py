def solution(s):
    answer = 1
    
    if s[0] == '+':
        answer *= 1
        answer *= int(s[1:])
    elif s[0] == '-':
        answer *= -1
        answer *= int(s[1:])
    else:
        answer *= int(s)
    return answer
  
  
"""
def strToInt(str):
    return int(str)
"""
