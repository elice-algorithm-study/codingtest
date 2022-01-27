def solution(new_id):
    answer = ''
    canWord = '-_.abcdefghijklmnopqrstuvwxyz1234567890'
    
    op1 = new_id.lower()
    
    op2 = op1
    for word in op2:
        if word not in canWord:
            op2 = op2.replace(word, "")
    
    op3 = op2
    if '.' in op3:
        while '..' in op3:
            op3 = op3.replace('..', '.')
    
    op4 = op3

    if op4[0] == '.':
        op4 = op4[1:]
    elif op4[-1] == '.':
        op4 = op4[:-1]
    
    op5 = op4
    if op5 == '':
        op5 = 'a'
    
    op6 = op5
    if len(op6)>15:
        op6 = op6[:15]
    if op6[-1]=='.':
        op6 = op6[:-1]

    op7 = op6
    while len(op7) < 3:
        op7 = op7 + op7[-1]
    
    answer = op7
    
    return answer
