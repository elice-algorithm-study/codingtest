def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if i==(len(arr)-2) and arr[i]==arr[i+1]:
            answer.append(arr[i])
            break
            
        elif i==(len(arr)-2) and arr[i]!=arr[i+1]:
            answer.append(arr[i])
            answer.append(arr[i+1])
            break
            
        if arr[i]==arr[i+1] and i < len(arr)-1:
            continue
        answer.append(arr[i])
    
    return answer
