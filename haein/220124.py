def solution(id_list, report, k): 
    answer = [0] * len(id_list)
    dic = {id:[] for id in id_list}
    
    for re in set(report): # 중복해제
        list = re.split()
        dic[list[1]].append(list[0])

    for key, val in dic.items(): # 키와 값들의 쌍을 하나씩 얻음
        if len(val) >= k:
            for v in val:
                answer[id_list.index(v)] += 1
        
    return answer