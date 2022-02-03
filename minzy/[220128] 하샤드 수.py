def solution(x):
    answer = True

    sum = 0

    for i in list(map(int, str(x))):
        sum += i

    return True if (x % sum == 0) else False