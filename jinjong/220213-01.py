def solution(n, lost, reserve):
    tmp_lost = list(set(lost) - set(reserve))
    tmp_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(tmp_lost)
    
    for num in tmp_lost:
        if (num-1) in tmp_reserve:
            tmp_reserve.remove(num-1)
            answer += 1
            continue
        elif (num+1) in tmp_reserve:
            tmp_reserve.remove(num+1)
            answer += 1
            continue
        
    return answer
