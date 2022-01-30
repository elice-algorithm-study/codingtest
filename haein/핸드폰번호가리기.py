def solution(phone_number):
    answer = ""
    result = []
    for i in range(len(phone_number)):
        if i >= len(phone_number) -4:
            result.append(phone_number[i])
        else:
            result.append("*")
    
    answer = "".join(result)
    
    return answer

# 다른 풀이
# answer = (len(phone_number)-4) * "*" + phone_number[-4:]