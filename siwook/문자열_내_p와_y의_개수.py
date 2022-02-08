def solution(s):
    answer = True
    s = s.lower()
    p_count = 0
    y_count = 0
    for i in range(len(s)):
        if s[i] == 'p':
            p_count += 1
        elif s[i] == 'y':
            y_count += 1
        else:
            continue
    
    if p_count != y_count:
        return False

    return True
  
  
"""
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
"""
