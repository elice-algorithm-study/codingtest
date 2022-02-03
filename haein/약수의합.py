def solution(n):
    answer = 0
    a = n
    numlist = []
    while a >= 1:
        if n % a == 0:
            if a not in numlist:
                numlist.append(a)
                if n/a not in numlist:
                    numlist.append(n/a)
            else:
                break
        a -= 1
    answer = sum(numlist)
        
    return answer