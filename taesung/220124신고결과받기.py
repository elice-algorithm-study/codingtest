def solution(id_list, report, k):
    answer = []
    pre_anser = {}
    # 딕셔너리 활용
    # set으로 중복 제거
    # split
    cnt_dict = {}
    dict = {}
    for d in id_list:
      pre_anser[d] = 0
      cnt_dict[d] = 0
      dict[d] = []
    # print(dict)

    # chk_list = [[] for i in range(len(id_list))]
    # print(chk_list)
    s_r = set(report)
    a_r = list(s_r)
    for a in a_r:
        r1, r2 = a.split(' ')
        cnt_dict[r2] += 1
        if r2 not in dict[r1]:
          dict[r1].append(r2)
    death = []
    for key in cnt_dict:
        if cnt_dict[key] >= k:
            death.append(key)
    # print(death)
    # print(dict)
    # print(cnt_dict)
    for d in death:
        for d_k in dict:
            if d in dict[d_k]:
                pre_anser[d_k] += 1
    # print(pre_anser)
    for pre in pre_anser:
        answer.append(pre_anser[pre])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))