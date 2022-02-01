def solution(s):
    spl = s.split(" ")
    answer = []
    
    for i in spl:
        a = ''
        for x in range(len(i)):
            
            if x % 2 == 0:
                a += i[x].upper()
            else: a += i[x].lower()
        answer.append(a)
    
    return ' '.join(answer)

