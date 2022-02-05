def solution(a, b):
    answer = ''
    data = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    for i in range(a):
        b += data[i]

    b %= 7
    answer += week[b]
    
    return answer
