def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        x = s[i]
        if x.islower():
            if ord(x) + n > 122:
                answer = answer + chr(ord(x)+n-26)
            else:
                answer = answer + chr(ord(x)+n)
        elif s[i].isupper():
            if ord(x) + n > 90:
                answer = answer + chr(ord(x)+n-26)
            else:
                answer = answer + chr(ord(x)+n)
        else:
            answer = answer + " "
    