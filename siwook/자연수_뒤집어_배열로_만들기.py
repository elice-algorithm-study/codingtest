def solution(n):
    answer = []
    
    n = list(map(int, list(str(n))))
    n.reverse()
    answer = n
    
    return answer
  
  
"""
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
"""
