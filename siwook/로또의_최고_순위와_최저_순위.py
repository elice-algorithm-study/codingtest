def solution(lottos, win_nums):
    answer = []
    rank = 7 # 순위와 당첨 갯수의 합이 7
    
    for i in lottos:
        for j in win_nums:
            #번호가 일치할 때마다 순위 상승
            if i == j:
                rank -= 1
    
    # rank를 7로 잡았기 때문에 rank가 6이상부터는 6등
    # 최고 순위: 0의 갯수만큼 순위 상승
    # 최저 순위: rank 그대로
    if rank - lottos.count(0) >= 6:
        answer.append(6)
    else:
        answer.append(rank - lottos.count(0))
        
    if rank >= 6:
        answer.append(6)
    else:
        answer.append(rank)
    
    return answer
