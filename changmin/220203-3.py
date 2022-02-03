def solution(n):
    num = 0
    cnt = 0
    strList = ['수', '박']
    a = ''
    while True:
        if cnt == n: break
        if num == 2:
            num = 0
        
        a += strList[num]
        cnt += 1
        num += 1
        
    return a


def solution(n):
    s = '수박' * n
    return s[:n]
