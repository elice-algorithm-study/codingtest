def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:])  # 비트연산 후 0b 제거

        if len(answer[i]) < n:  # 길이가 n보다 작으면 부족한 만큼 앞에 0 붙여줌
            answer[i] = '0' * (n - len(answer[i])) + answer[i]

        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')

    return answer