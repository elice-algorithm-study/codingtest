def solution(strings, n):
    answer = []

    # 1. 입력받은 배열의 단어들 맨 앞에, 인덱스 n번째 글자를 붙여준다
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    # 2. 변경된 배열을 sort해서 answer 배열에 넣어준다
    answer = sorted(strings)

    # 3. 다시 맨 앞의 인덱스 n번째 글자를 빼준다
    for j in range(len(answer)):
        answer[j] = answer[j][1:]

    return answer