def solution(s):
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = True
        for i in s:
            if i not in num:
                answer = False
    return answer
