def solution(arr):
    answer = []

    answer.append(arr[0])  # 맨 처음에 입력받은 배열의 첫 요소 넣고 시작

    for i in range(len(arr)):  # arr를 돌면서
        if arr[i] != answer[-1]:  # answer의 마지막 요소와 해당 요소가 다르면 추가
            answer.append(arr[i])

    return answer