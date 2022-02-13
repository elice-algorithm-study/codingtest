def solution(numbers):
    answer = 0
    data = [0] * 10
    
    for i in numbers:
        data[i] += 1
    
    for i in range(10):
        if data[i] == 0:
            answer += i
    return answer
  

"""
def solution(numbers):
    return 45 - sum(numbers)
"""
