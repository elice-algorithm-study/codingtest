def solution(s, n):
    answer = ''
    for c in s:
        if c!=' ' and ord(c) < 91:
            if ord(c) + n > 90:
                answer += chr(ord(c) + n - 26)
            else :
                answer += chr(ord(c) + n)
        elif c!=' ' and ord(c) > 96:
            if ord(c) + n > 122:
                answer += chr(ord(c) + n - 26)
            else :
                answer += chr(ord(c) + n)
        else:
            answer += " "
    return answer
