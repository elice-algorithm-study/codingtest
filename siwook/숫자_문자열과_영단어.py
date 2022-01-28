def solution(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    temp = ""
    
    # 포인터
    i = 0
    j = 1
    
    while True:
        # 종료조건
        if j == len(s) + 1:
            break
        
        # 숫자일 경우, 값 넣고 포인터 둘 다 이동
        if s[i].isdecimal():
            temp += s[i]
            i += 1
            j += 1
        # 숫자가 아닐 경우, 문자열 슬라이스 하면서 dic에 있는 지 확인
        else:
            # dic에 있을 경우, 숫자로 변환해서 넣고 뒤에 포인터를 앞에 포인터까지 이동 후 앞 포인터 + 1
            if s[i:j] in dic:
                temp += str(dic[s[i:j]])
                i = j
                j += 1
            # dic에 없을 경우, 앞 포인터만 + 1 
            else:
                j += 1
    answer = int(temp)
    return answer
  
  
"""
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""
