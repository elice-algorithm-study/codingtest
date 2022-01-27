import re

def solution(new_id):
    answer = ""
    # 1 단계
    new_id = new_id.lower()
    
    # 2 단계, 다른 특수문자 빈 문자열로 대체
    new_id = re.sub("[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]","",new_id)
    
    # 3 단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
         
    # 4 단계
    while len(new_id) > 0 :
            # 문자열.lstrip(인자): 인자로 전달된 문자를 문자열의 왼쪽에서 제거
        if new_id[0] == '.':
            new_id = new_id.lstrip('.')
        elif new_id[-1] == '.':
            # 문자열.lstrip(인자): 인자로 전달된 문자를 문자열의 오른쪽에서 제거
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


"""
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""
