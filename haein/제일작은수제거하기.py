def solution(arr):
    answer = []
    num = min(arr)
    
    if len(arr) == 1:
        answer = [-1]
    else :
        arr.pop(arr.index(num))
        for i in arr:
            answer.append(i)
    
    return answer