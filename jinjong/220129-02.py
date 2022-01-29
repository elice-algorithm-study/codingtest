def solution(x):
    str_x = str(x)
    sum = 0
    for i in range(len(str_x)):
        sum+=int(str_x[i])
    return True if x % sum == 0 else False
