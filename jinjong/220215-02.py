def solution(citations):
    answer = 0
    
    for i in range(len(citations), -1, -1):
        num = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                num += 1
        if num >= i:
            answer = i
            break
    return answer
