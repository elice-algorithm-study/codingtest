def solution(s):
    answer = 0

    # 숫자에 대응되는 영단어 표를 딕셔너리로 정리
    alphaToNum = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}

    # 딕셔너리를 돌면서
    for key, value in alphaToNum.items():
        if key in s: # key가 문자열 s에 포함되어 있다면
            s = s.replace(key, str(value)) # 문자형태로 변환된 value로 replace 해준다.

    answer = int(s) # 처음 선언된 answer가 숫자형이므로 int로 형변환 해준다.

    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))