def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer+='*'
    return answer + phone_number[-4:]
