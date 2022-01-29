def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer

'''
n * m 크기의 이차원 배열 초기화 방법
arr = [[0] * m for _ in range(n)]
'''