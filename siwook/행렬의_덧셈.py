def solution(arr1, arr2):
    column = len(arr1)
    row = len(arr1[0])
    answer = [[0] * row for i in range(column)]

    for i in range(column):
        for j in range(row):
            answer[i][j] += arr1[i][j] + arr2[i][j]
            
    return answer

  
"""
def sumMatrix(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer
"""
