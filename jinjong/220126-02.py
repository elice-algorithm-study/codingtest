def solution(s):
    numDict = {'zero': 0, 'one' : 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
              'seven':7, 'eight':8, 'nine':9}
    for value, key in numDict.items():
        if value in s:
            s = s.replace(value, str(key))
    answer = int(s)
    return answer
  
# def solution(s):
#   eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#   answer = ''
  
#   for i, num in enumerate(eng):
    
#     if num in s:
#       s = s.replace(num, str(i))
#     answer = s
    
#   return int(answer)
