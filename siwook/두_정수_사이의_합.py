def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    elif (abs(a - b) + 1) % 2 == 0:
        answer = (a + b) * (abs(a - b) + 1) / 2
    else:
        answer = (a + b) * abs(a - b) / 2 + (a + b) / 2
    return answer
  
  
"""
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))
"""
