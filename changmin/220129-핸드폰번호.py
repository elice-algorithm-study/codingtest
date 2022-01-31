def solution(phone_number):
    plen = len(phone_number)
    four = phone_number[-4:]
    answer = '*' * (plen - 4)    
    
    return answer + four