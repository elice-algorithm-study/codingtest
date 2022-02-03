def solution(id_list, report, k):
    answer = [0] * len(id_list) # id_list에 담긴 id 순서대로 출력하기 위해 id_list 길이만큼의 배열 생성
    report_dic = {}

    for id in id_list: # id_list에 있는 id를 key로 하는 dictionary 생성, value는 배열 형태
        report_dic[id] = []

    report = set(report) # set을 이용해서 동일한 유저에 대한 신고 횟수 중복 제거

    # 딕셔너리에 { user : user를 신고한 사람들 }의 형태로 담는다
    for user in report:
        report_dic[user.split(' ')[1]].append(user.split(' ')[0])

    for key, value in report_dic.items(): # 딕셔너리를 돌면서
        if len(value) >= k: # 주어진 k이상의 길이를 가진 value의 경우
            for people in value: # 해당 value에 담긴 사람들의 answer를 1씩 증가
                answer[id_list.index(people)] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","apeach frodo","apeach frodo","apeach frodo"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))