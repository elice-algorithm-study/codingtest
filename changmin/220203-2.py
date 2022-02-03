def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isSuper():
            s[i] = chr((ord(s[i]) -ord('A')+ n) % 26 + ord('A'))
        else:
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    
    return ''.join(s)



