def solution(lottos, win_nums):
    answer = []
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6}
    
    count = 0
    zcount = 0
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            zcount += 1
            
    if (count+zcount) <= 1 :
        answer.append(dic[1])
    else :
        answer.append(dic[count+zcount])
    
    if count <= 1:
        answer.append(dic[1])
    else:
        answer.append(dic[count])
    
    return answer