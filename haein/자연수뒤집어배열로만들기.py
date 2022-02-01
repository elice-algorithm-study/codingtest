def solution(n):
    answer = []
    length = len(str(n))

    for i in range(length):
        answer.append(int(str(n)[length-(i+1)]))
    
    return answer