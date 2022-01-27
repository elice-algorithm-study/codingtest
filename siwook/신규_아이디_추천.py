import re

def solution(new_id):
    answer = ""
    # 1 단계
    new_id = new_id.lower()
    
    # 2 단계
    new_id = re.sub("[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]","",new_id)
    
    # 3 단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
         
    # 4 단계
    while len(new_id) > 0 :
        if new_id[0] == '.':
            new_id = new_id.lstrip('.')
        elif new_id[-1] == '.':
            new_id = new_id.rstrip('.')    
        else:
            break


    # 5 단계
    if len(new_id) == 0:
        new_id += "a"

    # 6 단계
    while len(new_id) >= 16:
        new_id = list(new_id)
        new_id.pop()
        while new_id[-1] == '.':
            new_id.pop()
    new_id = ''.join(new_id)

    # 7 단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer += new_id
    return answer
