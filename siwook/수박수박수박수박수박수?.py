def solution(n):
    answer = ''
    
    if n % 2 == 0:
        answer += "수박" * int(n / 2)
    else:
        answer += "수박" * int(n / 2)
        answer += "수"
    
    return answer
  

"""
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
"""
