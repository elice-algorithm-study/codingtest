def solution(id_list, report, k):

    report = list(set(report))      # 중복 투표 제거    
    len_report = len(report)    
    
    data = [0] * len_report         # 신고 받은 횟수    
    answer = [0] * len(id_list)
    
    # 신고 받은 횟수 확인
    for i in range(len_report):
        data[id_list.index(report[i].split(' ')[1])] += 1
    
    for i in range(len_report):
        if data[i] >= k:                            # 신고 받은 횟수가 k 기준을 넘는다면
            for j in report:
                if id_list[i] == j.split(' ')[1]:   # 기준을 넘는 사람을 신고한 사람 결과 메일 + 1
                    answer[id_list.index(j.split(' ')[0])] += 1
    
    return answer
