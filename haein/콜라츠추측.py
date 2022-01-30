def solution(num):
    answer = 0
    count = 0
    while True:
        if num == 1 and count <= 500:
            answer = count
            break
        if num != 1 and count == 500:
            answer = -1
            break
        else :
            if num % 2 == 0:
                num = num / 2
                count += 1
            else:
                num = num * 3 + 1
                count += 1
                
    return answer