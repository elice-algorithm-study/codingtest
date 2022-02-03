def solution(lottos, win_nums):
    answer = []
    min = 0
    max = 0

    rank = { 0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1} # { 일치하는 수의 개수: 순위 } 형식으로 상단의 표 선언해주기

    for i in range(6):
        if win_nums[i] in lottos: # 일치하는 수의 개수만큼 min, max 변수에 각각 1씩 더해준다
            min += 1
            max += 1

        if lottos[i] == 0: # max 변수에는 lottos에 있는 0의 개수만큼 1씩 더 더해준다
            max += 1

    answer.append(rank[max])
    answer.append(rank[min])

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))