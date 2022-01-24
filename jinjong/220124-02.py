def solution(lottos, win_nums):
    zero_count = 0
    win_count = 0
    
    for num in lottos:
        if num==0:
            zero_count += 1    
        if num in win_nums:
            win_count += 1
            
    if win_count!=0:
        max_rank = 7 - win_count - zero_count
        min_rank = 7 - win_count
    else:
        if zero_count!=0:
            max_rank = 7 - zero_count
            min_rank = 6
        else:
            max_rank = 6
            min_rank = 6
    
    answer = [max_rank, min_rank]
    return answer
