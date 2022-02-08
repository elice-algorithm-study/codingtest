def solution(strings, n):
    answer = []
    
    strings.sort(key=lambda x: (x[n], x))
    answer = strings
    return answer
  
  
"""
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])
"""
