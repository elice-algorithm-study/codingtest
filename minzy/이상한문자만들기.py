def solution(s):
    answer = []

    s = s.split(' ')

    for word in s:
        new = ''
        for c in range(len(word)):
            if c % 2 == 0:
                new += word[c].upper()
            else:
                new += word[c].lower()
        answer.append(new)

    return ' '.join(answer)

'''
[ split()과 split(' ')의 차이 ]
split()
    - 주어진 모든 공백을 하나로 처리
    
split(' ')
    - 문자열 사이사이에 있는 공백만 배열의 분할점으로 이용
    - 공백이 연속해서 나오면 일반 문자 다음에 오는 공백을 제외한 나머지 공백 각가을 하나의 리스트 요소로 처리
    - 마지막에 분할할 요소가 없다면 남은 공백들을 전부 하나의 요소로 처리

출처 https://this-programmer.tistory.com/302
'''