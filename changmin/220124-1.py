def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n
    dict = {}
    s = [set() for i in range(n)]

    for i in range(n):
        dict[id_list[i]] = i
    
    for i in set(report):
        re_id, re_report = i.split()
        s[dict[re_report]].add(dict[re_id])
    
    for i in range(n):
        if len(s[i]) < k : continue
        for k in s[i] : answer[k] += 1

    return answer
