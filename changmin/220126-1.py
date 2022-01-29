new_id = "...!@BaT#*..y.abcdefghijklm"
new2= "z-+.^."
new3="=.="
new4="123_.def"
new5="abcdefghijklmn.p"

def solution(new_id):    
    answer = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.islower() or i.isdigit() or i in ['.', '-', '_']:
            answer += i
    
    while '..' in answer:
       answer = answer.replace('..', '.')

    if answer[0] == '.':
        if len(answer) >=2:
            answer = answer[1:]
        else:
            answer = '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
    
    if answer == '':
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    while len(answer) < 3:
        answer += answer[-1]
        if len(answer) >=3:
            break            
    
    return answer


