def solution(array, commands):
    answer = []

    # command 0번째 수 - 1 (인덱스) 부터 command 1번째 수까지 slice 후 정렬
    # answer에는 command[2] - 1 (인덱스) 에 있는 수를 출력
    for command in commands:
        answer.append(sorted(array[command[0] - 1: command[1]])[command[2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
