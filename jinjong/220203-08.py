import math

def solution(s):
    answer = ''
    tmp = []
    for a in s:
        tmp.append(ord(a))
        
    tmp.sort(reverse=True)
    
    for i in tmp:
        answer += chr(i)
    
    return answer
