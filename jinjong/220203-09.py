def solution(s):
    answer = True
    p = 0
    y = 0
    for a in s:
        if a == 'p' or a =='P':
            p+=1
        elif a == 'y' or a =='Y':
            y+=1
    if p==y:
        return True
    else :
        return False
