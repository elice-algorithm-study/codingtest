def solution(n):
    result = ''
    answer = 0

    while n != 0:
        result += str(n % 3)
        n = n // 3

    # 0021 => 1*1 + 2*3 + ...

    for i in range(len(result)):
        answer += int(result[i]) * (3 ** (len(result) - 1 - i))

    return answer
    # return int(result, 3)

print(solution(45))
print(solution(125))
