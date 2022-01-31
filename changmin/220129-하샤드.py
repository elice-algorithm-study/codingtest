def solution(x):
    result = 0
    for i in str(x):
        result += int(i)
    print(result, x)
    return x % result == 0


print(solution(10))