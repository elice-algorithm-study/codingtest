def solution(arr):
    answer = []
    
    if len(arr) <= 1:
        answer.append(-1)
    else:
        print(min(arr))
        arr.remove(min(arr))
        answer = arr
    return answer
