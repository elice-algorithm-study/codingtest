def solution(arr):
    answer = 0
    sum = 0

    for x in arr:
        sum += x
        answer = sum / len(arr)

    return answer