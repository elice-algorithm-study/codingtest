def solution(a, b):
    answer = 0
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a - 1): # 입력받은 월의 이전달까지의 일을 더해준다
        answer += month[i]

    answer += b # 입력받은 일을 더해준다
    answer = answer % 7 - 1

    return day[answer]