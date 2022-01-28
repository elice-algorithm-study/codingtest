def solution(new_id):
    answer = ''

    # 1. 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, - _ . 를 제외한 모든 문자 제거
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    while (True):
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break

    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    if (answer == '.'):  # 현재 문자열이 . 이라면 빈 문자열로 만들어준다.
        answer = ''
    else:
        if (answer[0] == '.'):
            answer = answer[1:]
        if (answer[-1] == '.'):
            answer = answer[:-1]

    # 5. 빈 문자열이라면, a를 대입
    if (answer == ''):
        answer += 'a'

    # 6. 길이가 16자 이상이면, 15개 이외 문자 제거
    if (len(answer) >= 16):
        answer = answer[:15]
        if (answer[-1] == '.'):
            answer = answer[:-1]

    # 7. 길이가 2자 이하면, 3이 될 때까지 문자 반복
    if (len(answer) <= 2):
        while (len(answer) < 3):
            answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))