def solution(arr):
    answer = []
   
    if len(arr) == 1:
        answer = arr
    else:
        i = 0
        j = 1
        while j < len(arr):            
            if arr[i] == arr[j]:
                j += 1
            else:
                answer += arr[j - 1: j]
                i = j
                j = i + 1
        answer.append(arr[i])
    return answer
  
 
"""
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
"""
