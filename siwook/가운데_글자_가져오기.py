def solution(s):
    answer = ''

    length = len(s)
    if length % 2 == 0:
        answer += s[length // 2 - 1]
        answer += s[length // 2]
    else:
        answer += s[length // 2]
    
    return answer
  
  
"""
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]
"""
