def solution(answers):
    answer = []

    # student 1, 2, 3의 패턴을 answers 길이에 맞춰 생성
    student1 = ([1, 2, 3, 4, 5] * (len(answers) // 5)) + ([1, 2, 3, 4, 5][:len(answers) % 5])
    student2 = ([2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8)) + ([2, 1, 2, 3, 2, 4, 2, 5][:len(answers) % 8])
    student3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10)) + (
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:len(answers) % 10])

    # 각 학생의 답이 answers와 일치한다면 answer에 학생을 append
    for i in range(len(student1)):
        if answers[i] == student1[i]:
            answer.append(1)

    for j in range(len(student2)):
        if answers[j] == student2[j]:
            answer.append(2)

    for k in range(len(student3)):
        if answers[k] == student3[k]:
            answer.append(3)

    # 각 학생이 맞춘 답의 갯수를 count해서 새로운 리스트 생성
    answer_cnt = [answer.count(1), answer.count(2), answer.count(3)]

    # 맞춘 답의 갯수와 maximum 값이 일치하면 result에 해당 학생의 인덱스 + 1을 추가
    result = [l + 1 for l in range(len(answer_cnt)) if answer_cnt[l] == max(answer_cnt)]

    return result

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
