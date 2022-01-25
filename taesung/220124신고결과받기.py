def solution(id_list, report, k):
    answer = []
    # tab(줄간격)이 프로그래머스와 달라 보정 해주셔야 프로그래머스 통과합니다.

    # 정답 전 k개 이상의 신고를 받아 사망한 자에게 투표한 수를 넣을 딕셔너리
    pre_anser = {}

    # 사망자를 걸러내기 위해 신고 당한 수를 담을 딕셔너리
    cnt_dict = {}

    # 본인이 신고한 사람 이름을 담을 배열을 타입으로 가진 딕셔너리
    # 그냥 숫자나 인덱스면 좋을텐데 문자여서 어려웠네요 ;;
    dict = {}
    for d in id_list:
      pre_anser[d] = 0
      cnt_dict[d] = 0
      dict[d] = []
    # print(dict)

    # set는 중복을 자동으로 제거해줍니다.
    # 하지만 원치 않는 순서도 abcd 로 정렬됩니다.
    s_r = set(report)
    a_r = list(s_r)

    # set도 반복이 가능할테지만 익숙한 리스트로 바꿔줬습니다.
    for a in a_r:
        # 파이썬은 변수 두개를 한번에 할당이 가능합니다.
        r1, r2 = a.split(' ')
        # 신고당한 사람 카운팅
        cnt_dict[r2] += 1
        # 지금 생각해보니 set로 중복을 없애줘서 이 조건문은 없어도 될 것 같습니다.
        if r2 not in dict[r1]:
          dict[r1].append(r2)
    # 사망자 명단을 담을 빈 배열
    death = []
    # 신고 카운팅 딕셔너리를 반복문을 돌려 value값이 k보다 큰지를 체크해줍니다.
    for key in cnt_dict:
        if cnt_dict[key] >= k:
            death.append(key)
    # print(death)
    # print(dict)
    # print(cnt_dict)

    # 사망자 명단과 사망자를 지명한 명단 딕셔너리를 비교하여 pre_answer(밑에 anser라고 오타 ;; 다행) 에 넣어줍니다.
    for d in death:
        for d_k in dict:
            if d in dict[d_k]:
                pre_anser[d_k] += 1
    # print(pre_anser)

    # 출력 형식에 맞게 배열로 예쁘게 만들어주기
    for pre in pre_anser:
        answer.append(pre_anser[pre])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))