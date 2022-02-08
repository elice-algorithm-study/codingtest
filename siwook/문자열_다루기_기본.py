def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return answer
            
        except ValueError:
            return False
    else:
        return False
      
      
"""
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
"""
