def solution(phone_number):
    answer = ''

    for i in range(len(phone_number) - 4):
        answer += '*'

    answer += phone_number[-4:]

    return answer


print(solution("01012345678"))

'''
문자열의 곱셈 풀이
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
'''