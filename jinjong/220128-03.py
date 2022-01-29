def solution(arr1, arr2):
    answer = []
    tmp = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
        tmp = []
    return answer
